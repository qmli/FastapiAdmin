from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base_model import MappedBase


class SysCacheModel(MappedBase):
    """Redis 关闭时的键值表：会话、参数缓存、字典缓存、验证码、锁都写在这里。"""

    __tablename__ = "sys_cache"
    __table_args__ = {"comment": "键值存储（Redis 关闭时会话、缓存、锁、验证码直接落库）"}

    cache_key: Mapped[str] = mapped_column(String(640), primary_key=True, comment="键")
    cache_value: Mapped[str] = mapped_column(
        Text().with_variant(MEDIUMTEXT(), "mysql"),
        nullable=False,
        comment="值",
    )
    expire_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        index=True,
        comment="过期时间（UTC），空表示不过期",
    )
