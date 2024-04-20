# coding=utf-8
from src.model.future.miaowa.compontent.cmd.ReviewAndFollowCmdExecutor import ReviewAndFollowCmdExecutor


# cmd管理器
class CmdManager:
    _raf = ReviewAndFollowCmdExecutor()
    # 类型实现
    __impl = {
        "raf": _raf
    }

    @staticmethod
    def get_instance(impl):
        return CmdManager.__impl.get(impl)


