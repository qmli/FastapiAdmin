"""日志保留清理内置处理器。

节点 func 使用 ``builtin:log_cleanup.handler``，不经过 exec，
因此在 ``SCHEDULER_ALLOW_CODE_EXEC=false`` 时仍可调度。
"""

import asyncio


def handler(*args, **kwargs) -> dict:
    """按保留天数清理过期操作日志与登录日志。

    参数:
    - kwargs: 支持 ``days``（保留天数，默认 90）。

    返回:
    - dict: 各表清理条数。
    """
    from app.modules.system.log.service import cleanup_expired_logs

    days = int(kwargs.get("days", 90) or 90)
    return asyncio.run(cleanup_expired_logs(days=days))


HANDLERS = {"handler": handler}
