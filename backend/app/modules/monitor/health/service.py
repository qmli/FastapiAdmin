"""健康检查服务：仅探测 DB / Redis 网络连通（SELECT 1 / PING）。"""

import asyncio
from typing import Any

from sqlalchemy import text

from app.config.setting import settings
from app.core.database import async_db_session
from app.core.logger import logger

from .schema import ServiceInfoOut


class HealthService:
    """健康检查服务：探测 DB / Redis 网络连通并组装状态。"""

    @classmethod
    async def check_database(cls) -> int:
        """数据库连通：SELECT 1 成功返回 1，失败返回 0。"""
        try:
            async with async_db_session() as session:
                await session.execute(text("SELECT 1"))
            return 1
        except Exception as e:
            logger.warning(f"数据库连通检查失败: {e}")
            return 0

    @classmethod
    async def check_redis(cls, redis: Any | None) -> int:
        """Redis 连通。PING 已注释（lqm rm），不是删除；当前不探测，记为正常（缓存走数据库）。"""
        return 1
        # lqm rm 原 Redis PING（已注释，不是删除）。恢复时取消下面注释，并删除上面的 return。
        # if redis is None:
        #     return 0
        # try:
        #     await redis.ping()
        #     return 1
        # except Exception as e:
        #     logger.warning(f"Redis 连通检查失败: {e}")
        #     return 0

    @classmethod
    async def collect(cls, redis: Any | None) -> ServiceInfoOut:
        """并行探活 DB / Redis，组装健康状态。"""
        db_status, redis_status = await asyncio.gather(
            cls.check_database(),
            cls.check_redis(redis),
        )
        return ServiceInfoOut(
            name=settings.TITLE,
            version=settings.VERSION,
            environment=settings.ENVIRONMENT.value,
            db_status=db_status,
            redis_status=redis_status,
            # 升级可见性：这两个开关会静默改变行为（代码块任务不可调度 / 生产拒绝全部跨域），
            # 在健康检查里显式暴露，避免运维只看到"任务不动了"而不知原因。
            code_exec_enabled=settings.SCHEDULER_ALLOW_CODE_EXEC,
            cors_origins_configured=bool(settings.PROD_CORS_ORIGINS) if settings.ENVIRONMENT.value == "prod" else True,
        )
