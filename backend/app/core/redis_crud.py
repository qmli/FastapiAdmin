from typing import Any

from fastapi import FastAPI
from redis import exceptions  # noqa: F401  # lqm rm 下方连接代码已注释，保留导入，不是删除
from redis.asyncio import Redis

from app.config.setting import settings  # noqa: F401  # lqm rm 下方注释中的 Redis 连接仍引用它，保留导入，不是删除
from app.core import db_cache
from app.core.logger import logger

# lqm rm Redis 客户端调用已整段注释，不是强制删除。当前会话/缓存/锁直接读写数据库表 sys_cache。
# lqm rm 恢复：取消本文件中「lqm rm 原 Redis」注释，并把 REDIS_ENABLE 改回 true（同时恢复 docker-compose 里的 Redis 服务注释）。


async def redis_connect(app: FastAPI, status: bool) -> Redis | None:
    """创建或关闭 Redis 连接。

    连接实现已注释（lqm rm），不是删除。当前不访问 Redis，调用方改走数据库键值表。

    参数:
    - app (FastAPI): FastAPI应用实例。
    - status (bool): 连接状态,True为创建连接,False为关闭连接。

    返回:
    - Redis | None: 当前固定返回 None。
    """
    if status:
        app.state.redis = None
    return None
    # lqm rm 原 Redis 连接（已注释，不是删除）。恢复时取消本段注释，并删除上面的提前 return。
    # if status:
    #     try:
    #         rd = await Redis.from_url(
    #             url=settings.REDIS_URI,
    #             encoding="utf-8",
    #             decode_responses=True,
    #             health_check_interval=settings.REDIS_HEALTH_CHECK_INTERVAL,
    #             max_connections=settings.POOL_SIZE,
    #             socket_timeout=settings.POOL_TIMEOUT,
    #         )
    #         app.state.redis = rd
    #         if await rd.ping():
    #             return rd
    #         msg = "Redis ping 返回 False，连接不可用"
    #         raise exceptions.ConnectionError(msg)
    #     except exceptions.RedisError as e:
    #         logger.error(f"❌ Redis 连接失败: {e}")
    #         raise
    # else:
    #     await app.state.redis.close()
    #     logger.info("✅️ Redis连接已关闭")


class RedisCURD:
    """缓存工具类。Redis 读写已注释（lqm rm），不是删除；当前方法全部直接读写数据库。"""

    redis: Redis

    def __init__(self, redis: Redis | None) -> None:
        """初始化。Redis 关闭时 ``redis`` 可以为空，读写走数据库。"""
        self.redis = redis  # type: ignore[assignment]

    async def mget(self, keys: list) -> list:
        """批量获取缓存

        参数:
        - keys (list): 键名列表

        返回:
        - list: 返回缓存值列表,如果获取失败则返回空列表
        """
        try:
            # lqm rm 原 Redis：data = await self.redis.mget(...) 已注释，不是删除。
            return await db_cache.cache_mget(keys)
            # data = await self.redis.mget(*[str(key) for key in keys])
            # return data
        except Exception as e:
            logger.error(f"批量获取缓存失败: {e!s}")
            return []

    async def scan_keys(self, pattern: str = "*", count: int = 100) -> list:
        """SCAN 模式获取缓存键名（不阻塞 Redis，推荐替代 get_keys）

        参数:
        - pattern (str, optional): 匹配模式,默认值为"*"。
        - count (int, optional): 每次迭代基数，默认 100。

        返回:
        - list: 返回匹配的缓存键名列表,如果获取失败则返回空列表
        """
        try:
            # lqm rm 原 Redis：scan_iter 已注释，不是删除。
            return await db_cache.cache_keys(pattern)
            # keys: list = []
            # async for key in self.redis.scan_iter(match=pattern, count=count):
            #     keys.append(key)
            # return keys
        except Exception as e:
            logger.error(f"扫描缓存键名失败: {e!s}")
            return []

    async def get_keys(self, pattern: str = "*") -> list:
        """获取缓存键名（KEYS 命令，可能阻塞 Redis，小数据量使用）

        参数:
        - pattern (str, optional): 匹配模式,默认值为"*"。

        返回:
        - list: 返回匹配的缓存键名列表,如果获取失败则返回空列表
        """
        try:
            # lqm rm 原 Redis：keys 命令已注释，不是删除。
            return await db_cache.cache_keys(pattern)
            # keys = await self.redis.keys(f"{pattern}")
            # return keys
        except Exception as e:
            logger.error(f"获取缓存键名失败: {e!s}")
            return []

    async def get(self, key: str) -> Any:
        """获取缓存

        参数:
        - key (str): 缓存键名

        返回:
        - Any: 返回缓存值,如果缓存不存在则返回None
        """
        try:
            # lqm rm 原 Redis：await self.redis.get 已注释，不是删除。
            return await db_cache.cache_get(key)
            # data = await self.redis.get(f"{key}")
            # if data is None:
            #     return None
            # return data
        except Exception as e:
            logger.error(f"获取缓存失败: {e!s}")
            return None

    async def set(self, key: str, value: Any, expire: int | None = None) -> bool:
        """设置缓存

        参数:
        - key (str): 缓存键名
        - value (Any): 缓存值
        - expire (int, optional): 过期时间,单位为秒,默认值为None

        返回:
        - bool: 如果设置缓存成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.set 已注释，不是删除。
            return await db_cache.cache_set(key, value, expire)
            # if expire:
            #     await self.redis.set(name=key, value=value, ex=expire)
            # else:
            #     await self.redis.set(name=key, value=value)
            # return True
        except Exception as e:
            logger.error(f"设置缓存失败: {e!s}")
            return False

    async def compare_and_set(self, key: str, expected: str, value: str, expire: int) -> bool:
        """原子替换：仅当键当前值与 expected 完全一致时写入 value。

        用于「读-改-写」场景：键被并发修改、删除（如已登出的会话）时写入会被跳过，
        既不会覆盖他人更新，也不会让已删除的键复活。

        参数:
        - key (str): 缓存键名
        - expected (str): 读取到的原值
        - value (str): 待写入的新值
        - expire (int): 新值的过期时间(秒)

        返回:
        - bool: 写入成功返回True，键已变化/不存在或出错返回False
        """
        try:
            # lqm rm 原 Redis Lua 原子替换已注释，不是删除。
            return await db_cache.cache_compare_and_set(key, expected, value, expire)
            # script = """
            # if redis.call('get', KEYS[1]) ~= ARGV[1] then
            #     return 0
            # end
            # redis.call('set', KEYS[1], ARGV[2], 'EX', tonumber(ARGV[3]))
            # return 1
            # """
            # result = await self.redis.eval(script, 1, key, expected, value, expire)
            # return result == 1
        except Exception as e:
            logger.error(f"原子更新缓存失败: {key}: {e!s}")
            return False

    async def lock(self, key: str, expire: int, value: str | None = None) -> tuple[bool, str]:
        """获取分布式锁

        参数:
        - key (str): 锁键名
        - expire (int): 锁过期时间,单位为秒
        - value (str, optional): 锁值,默认值为None（自动生成UUID）。

        返回:
        - tuple[bool, str]: (获取锁是否成功, 锁值)
        """
        try:
            import uuid

            # 如果没有提供value，生成唯一的UUID
            lock_value = value or str(uuid.uuid4())
            # lqm rm 原 Redis SET NX 已注释，不是删除。
            acquired = await db_cache.cache_lock(key, expire, lock_value)
            return (acquired, lock_value if acquired else "")
            # result = await self.redis.set(
            #     name=key,
            #     value=lock_value,
            #     ex=expire,
            #     nx=True,  # 只有当键不存在时才设置
            # )
            # return (result is not None, lock_value)
        except Exception as e:
            logger.error(f"获取分布式锁失败: {e!s}")
            return (False, "")

    async def unlock(self, key: str, value: str) -> bool:
        """释放分布式锁（安全版本，验证锁值）

        参数:
        - key (str): 锁键名
        - value (str): 锁值，用于验证锁的持有者

        返回:
        - bool: 如果释放锁成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis Lua 解锁已注释，不是删除。
            return await db_cache.cache_unlock(key, value)
            # script = """
            # if redis.call('get', KEYS[1]) == ARGV[1] then
            #     return redis.call('del', KEYS[1])
            # else
            #     return 0
            # end
            # """
            # result = await self.redis.eval(script, 1, key, value)
            # return result == 1
        except Exception as e:
            logger.error(f"释放分布式锁失败: {e!s}")
            return False

    async def unlock_simple(self, key: str) -> bool:
        """释放分布式锁（简单版本，不验证锁值）

        参数:
        - key (str): 锁键名

        返回:
        - bool: 如果释放锁成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.delete(key) 已注释，不是删除。
            return await db_cache.cache_delete(key)
            # await self.redis.delete(key)
            # return True
        except Exception as e:
            logger.error(f"释放分布式锁失败: {e!s}")
            return False

    async def delete(self, *keys: str) -> bool:
        """删除缓存

        参数:
        - keys (str): 缓存键名

        返回:
        - bool: 如果删除缓存成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.delete(*keys) 已注释，不是删除。
            return await db_cache.cache_delete(*keys)
            # await self.redis.delete(*keys)
            # return True
        except Exception as e:
            logger.error(f"删除缓存失败: {e!s}")
            return False

    async def clear(self, pattern: str = "*") -> bool:
        """清空缓存

        参数:
        - pattern (str, optional): 匹配模式,默认值为"*"。

        返回:
        - bool: 如果清空缓存成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：keys + delete 已注释，不是删除。
            keys = await db_cache.cache_keys(pattern)
            if keys:
                await db_cache.cache_delete(*keys)
            return True
            # keys = await self.redis.keys(f"{pattern}")
            # if keys:
            #     await self.redis.delete(*keys)
            # return True
        except Exception as e:
            logger.error(f"清空缓存失败: {e!s}")
            return False

    async def exists(self, key: str) -> bool:
        """判断缓存是否存在

        参数:
        - key (str): 缓存键名

        返回:
        - bool: 如果缓存存在则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.exists 已注释，不是删除。
            return await db_cache.cache_exists(key)
            # return await self.redis.exists(f"{key}")
        except Exception as e:
            logger.error(f"判断缓存是否存在失败: {e!s}")
            return False

    async def ttl(self, key: str) -> int:
        """获取缓存过期时间

        参数:
        - key (str): 缓存键名

        返回:
        - int: 返回缓存过期时间,单位为秒,如果缓存没有设置过期时间则返回-1
        """
        try:
            # lqm rm 原 Redis：await self.redis.ttl 已注释，不是删除。
            return await db_cache.cache_ttl(key)
            # return await self.redis.ttl(f"{key}")
        except Exception as e:
            logger.error(f"获取缓存过期时间失败: {e!s}")
            return -1

    async def renew_lock(self, key: str, expire: int, value: str) -> bool:
        """续约分布式锁

        参数:
        - key (str): 锁键名
        - expire (int): 新的过期时间,单位为秒
        - value (str): 锁值，用于验证锁的持有者

        返回:
        - bool: 如果续约锁成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis Lua 续约已注释，不是删除。
            return await db_cache.cache_renew_lock(key, expire, value)
            # script = """
            # if redis.call('get', KEYS[1]) == ARGV[1] then
            #     return redis.call('expire', KEYS[1], ARGV[2])
            # else:
            #     return 0
            # end
            # """
            # result = await self.redis.eval(script, 1, key, value, str(expire))
            # return result == 1
        except Exception as e:
            logger.error(f"续约分布式锁失败: {e!s}")
            return False

    async def expire(self, key: str, expire: int) -> bool:
        """设置缓存过期时间

        参数:
        - key (str): 缓存键名
        - expire (int): 过期时间,单位为秒

        返回:
        - bool: 如果设置缓存过期时间成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.expire 已注释，不是删除。
            return await db_cache.cache_expire(key, expire)
            # return bool(await self.redis.expire(name=key, time=expire))
        except Exception as e:
            logger.error(f"设置缓存过期时间失败: {e!s}")
            return False

    async def delete_by_pattern(self, pattern: str) -> int:
        """按 glob 模式批量删除 Redis 键，返回实际删除的键数

        参数:
        - pattern (str): 通配符模式，例如 "USER_SESSION:123*"

        返回:
        - int: 实际删除的键数量
        """
        try:
            # lqm rm 原 Redis：scan_iter + delete 已注释，不是删除。
            keys = await db_cache.cache_keys(pattern)
            if keys:
                await db_cache.cache_delete(*keys)
            return len(keys)
            # count = 0
            # async for key in self.redis.scan_iter(match=pattern, count=100):
            #     if await self.redis.delete(key):
            #         count += 1
            # return count
        except Exception as e:
            logger.error(f"按模式删除缓存失败: pattern={pattern}, err={e!s}")
            return 0

    async def info(self) -> dict:
        """获取缓存信息

        返回:
        - dict: 返回缓存信息字典,如果获取失败则返回空字典
        """
        try:
            # lqm rm 原 Redis：await self.redis.info() 已注释，不是删除。
            return await db_cache.cache_info()
            # return await self.redis.info()
        except Exception as e:
            logger.error(f"获取缓存信息失败: {e!s}")
            return {}

    async def db_size(self) -> int:
        """获取数据库大小

        返回:
        - int: 返回数据库大小,如果获取失败则返回0
        """
        try:
            # lqm rm 原 Redis：await self.redis.dbsize() 已注释，不是删除。
            return await db_cache.cache_db_size()
            # return await self.redis.dbsize()
        except Exception as e:
            logger.error(f"获取数据库大小失败: {e!s}")
            return 0

    async def commandstats(self) -> dict:
        """获取命令统计信息

        返回:
        - dict: 返回命令统计信息字典,如果获取失败则返回空字典
        """
        try:
            # lqm rm 原 Redis：await self.redis.info("commandstats") 已注释，不是删除。数据库模式无命令统计。
            return {}
            # return await self.redis.info("commandstats")
        except Exception as e:
            logger.error(f"获取命令统计信息失败: {e!s}")
            return {}

    async def hash_set(self, name: str, key: str, value: Any) -> bool:
        """设置哈希缓存

        参数:
        - name (str): 哈希缓存名称
        - key (str): 哈希缓存键名
        - value (Any): 哈希缓存值

        返回:
        - bool: 如果设置哈希缓存成功则返回True,否则返回False
        """
        try:
            # lqm rm 原 Redis：await self.redis.hset 已注释，不是删除。
            return await db_cache.cache_hash_set(name, key, value)
            # await self.redis.hset(name=name, key=key, value=value)
            # return True
        except Exception as e:
            logger.error(f"设置哈希缓存失败: {e!s}")
            return False

    async def hash_get(self, name: str, keys: list[str]) -> list[Any]:
        """获取哈希缓存

        参数:
        - name (str): 哈希缓存名称
        - keys (list[str]): 哈希缓存键名列表

        返回:
        - Awaitable[list[Any]] | list[Any]: 返回哈希缓存值列表,如果获取失败则返回空列表
        """
        try:
            # lqm rm 原 Redis：await self.redis.hmget 已注释，不是删除。
            return await db_cache.cache_hash_get(name, keys)
            # data = await self.redis.hmget(name=name, keys=keys)
            # return data
        except Exception as e:
            logger.error(f"获取哈希缓存失败: {e!s}")
            return []

    async def publish(self, channel: str, message: str) -> int:
        """发布消息到频道（Redis pub/sub）

        参数:
        - channel (str): 频道名称
        - message (str): 消息内容

        返回:
        - int: 订阅者数量
        """
        try:
            # lqm rm 原 Redis：await self.redis.publish 已注释，不是删除。单进程推送不依赖它。
            return 0
            # return await self.redis.publish(channel, message)
        except Exception as e:
            logger.error(f"Redis 发布消息失败: channel={channel}, err={e!s}")
            return 0
