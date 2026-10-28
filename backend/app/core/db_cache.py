"""Redis 关闭时的数据库键值存储。

语义对齐 Redis 字符串命令：过期键读取时视为不存在；``expire`` 为空表示永不过期。
"""

from datetime import UTC, datetime, timedelta
from typing import Any

from sqlalchemy import delete, func, or_, select, update
from sqlalchemy.exc import IntegrityError

from app.config.setting import settings
from app.core.database import async_db_session
from app.core.kvstore.model import SysCacheModel


def _aware(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


def _expired(expire_at: datetime | None, now: datetime) -> bool:
    if expire_at is None:
        return False
    return _aware(expire_at) <= now


def _deadline(expire: int | None) -> datetime | None:
    if not expire:
        return None
    return datetime.now(UTC) + timedelta(seconds=int(expire))


def _stringify(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode()
    return str(value)


def _glob_to_like(pattern: str) -> str:
    """把 Redis glob（* ?）转成 SQL LIKE，并转义字面量里的 % _ \\。"""
    out: list[str] = []
    for ch in pattern:
        if ch == "*":
            out.append("%")
        elif ch == "?":
            out.append("_")
        elif ch in "%_\\":
            out.append("\\" + ch)
        else:
            out.append(ch)
    return "".join(out)


def _live_clause(now: datetime):
    return or_(SysCacheModel.expire_at.is_(None), SysCacheModel.expire_at > now)


async def cache_get(key: str) -> str | None:
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        row = await session.get(SysCacheModel, key)
        if row is None:
            return None
        if _expired(row.expire_at, now):
            await session.delete(row)
            return None
        return row.cache_value


async def cache_mget(keys: list) -> list:
    if not keys:
        return []
    str_keys = [str(key) for key in keys]
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        rows = (await session.execute(select(SysCacheModel).where(SysCacheModel.cache_key.in_(str_keys)))).scalars().all()
        found: dict[str, str] = {}
        for row in rows:
            if _expired(row.expire_at, now):
                await session.delete(row)
                continue
            found[row.cache_key] = row.cache_value
    return [found.get(key) for key in str_keys]


async def cache_set(key: str, value: Any, expire: int | None = None) -> bool:
    stored = _stringify(value)
    expire_at = _deadline(expire)
    try:
        async with async_db_session() as session, session.begin():
            row = await session.get(SysCacheModel, key)
            if row is None:
                session.add(SysCacheModel(cache_key=key, cache_value=stored, expire_at=expire_at))
            else:
                row.cache_value = stored
                row.expire_at = expire_at
        return True
    except IntegrityError:
        async with async_db_session() as session, session.begin():
            row = await session.get(SysCacheModel, key)
            if row is None:
                session.add(SysCacheModel(cache_key=key, cache_value=stored, expire_at=expire_at))
            else:
                row.cache_value = stored
                row.expire_at = expire_at
        return True


async def cache_delete(*keys: str) -> bool:
    if not keys:
        return True
    async with async_db_session() as session, session.begin():
        await session.execute(delete(SysCacheModel).where(SysCacheModel.cache_key.in_(list(keys))))
    return True


async def cache_keys(pattern: str = "*") -> list[str]:
    now = datetime.now(UTC)
    like = _glob_to_like(pattern)
    async with async_db_session() as session, session.begin():
        await session.execute(
            delete(SysCacheModel).where(
                SysCacheModel.expire_at.is_not(None),
                SysCacheModel.expire_at <= now,
            )
        )
        rows = (
            await session.execute(
                select(SysCacheModel.cache_key).where(
                    SysCacheModel.cache_key.like(like, escape="\\"),
                    _live_clause(now),
                )
            )
        ).all()
    return [row[0] for row in rows]


async def cache_exists(key: str) -> bool:
    return await cache_get(key) is not None


async def cache_ttl(key: str) -> int:
    """与 Redis TTL 一致：不存在返回 -2，永不过期返回 -1，否则返回剩余秒数。"""
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        row = await session.get(SysCacheModel, key)
        if row is None:
            return -2
        if row.expire_at is None:
            return -1
        if _expired(row.expire_at, now):
            await session.delete(row)
            return -2
        return max(int((_aware(row.expire_at) - now).total_seconds()), 0)


async def cache_expire(key: str, expire: int) -> bool:
    deadline = _deadline(expire)
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        result = await session.execute(update(SysCacheModel).where(SysCacheModel.cache_key == key, _live_clause(now)).values(expire_at=deadline))
    return result.rowcount == 1


async def cache_compare_and_set(key: str, expected: str, value: str, expire: int) -> bool:
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        result = await session.execute(
            update(SysCacheModel)
            .where(
                SysCacheModel.cache_key == key,
                SysCacheModel.cache_value == expected,
                _live_clause(now),
            )
            .values(cache_value=value, expire_at=_deadline(expire))
        )
    return result.rowcount == 1


async def cache_lock(key: str, expire: int, value: str) -> bool:
    now = datetime.now(UTC)
    deadline = _deadline(expire)
    try:
        async with async_db_session() as session, session.begin():
            row = await session.get(SysCacheModel, key)
            if row is not None and not _expired(row.expire_at, now):
                return False
            if row is not None:
                row.cache_value = value
                row.expire_at = deadline
                return True
            session.add(SysCacheModel(cache_key=key, cache_value=value, expire_at=deadline))
        return True
    except IntegrityError:
        return False


async def cache_unlock(key: str, value: str) -> bool:
    async with async_db_session() as session, session.begin():
        result = await session.execute(
            delete(SysCacheModel).where(
                SysCacheModel.cache_key == key,
                SysCacheModel.cache_value == value,
            )
        )
    return result.rowcount == 1


async def cache_renew_lock(key: str, expire: int, value: str) -> bool:
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        result = await session.execute(
            update(SysCacheModel)
            .where(
                SysCacheModel.cache_key == key,
                SysCacheModel.cache_value == value,
                _live_clause(now),
            )
            .values(expire_at=_deadline(expire))
        )
    return result.rowcount == 1


async def cache_incr(key: str, window_seconds: int) -> int:
    """固定窗口计数。键不存在或已过期时从 1 重新计，并套上窗口 TTL。"""
    for attempt in range(2):
        try:
            return await _incr_once(key, window_seconds)
        except IntegrityError:
            if attempt == 1:
                raise
    return 1


async def _incr_once(key: str, window_seconds: int) -> int:
    now = datetime.now(UTC)
    async with async_db_session() as session, session.begin():
        row = await session.get(SysCacheModel, key, with_for_update=True)
        if row is None or _expired(row.expire_at, now):
            if row is not None:
                row.cache_value = "1"
                row.expire_at = _deadline(window_seconds)
            else:
                session.add(
                    SysCacheModel(
                        cache_key=key,
                        cache_value="1",
                        expire_at=_deadline(window_seconds),
                    )
                )
            return 1
        count = int(row.cache_value) + 1
        row.cache_value = str(count)
        return count


async def cache_db_size() -> int:
    now = datetime.now(UTC)
    async with async_db_session() as session:
        result = await session.execute(select(func.count()).select_from(SysCacheModel).where(_live_clause(now)))
    return int(result.scalar_one() or 0)


def _human_bytes(size: int) -> str:
    if size < 1024:
        return f"{size}B"
    if size < 1024 * 1024:
        return f"{size / 1024:.2f}K"
    return f"{size / 1024 / 1024:.2f}M"


async def cache_info() -> dict:
    now = datetime.now(UTC)
    async with async_db_session() as session:
        result = await session.execute(
            select(
                func.count(),
                func.coalesce(func.sum(func.length(SysCacheModel.cache_value)), 0),
            ).where(_live_clause(now))
        )
        count, nbytes = result.one()
    return {
        "redis_version": "disabled",
        "redis_mode": "database",
        "os": settings.DATABASE_TYPE,
        "tcp_port": settings.DATABASE_PORT,
        "used_memory_human": _human_bytes(int(nbytes or 0)),
        "connected_clients": 0,
        "uptime_in_days": 0,
        "db_keys": int(count or 0),
    }


async def cache_hash_set(name: str, key: str, value: Any) -> bool:
    import json

    raw = await cache_get(name)
    try:
        data = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        data = {}
    data[key] = _stringify(value)
    return await cache_set(name, json.dumps(data, ensure_ascii=False), expire=None)


async def cache_hash_get(name: str, keys: list[str]) -> list[Any]:
    import json

    raw = await cache_get(name)
    try:
        data = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        data = {}
    if not isinstance(data, dict):
        return [None for _ in keys]
    return [data.get(key) for key in keys]
