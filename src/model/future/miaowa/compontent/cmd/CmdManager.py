# coding=utf-8
from src.model.future.miaowa.compontent.cmd.ReviewAndFollowCmdExecutor import ReviewAndFollowCmdExecutor
from src.model.future.miaowa.compontent.cmd.StoreDataCmdExecutor import StoreDataCmdExecutor


# cmd管理器
class CmdManager:
    _raf = ReviewAndFollowCmdExecutor()
    _sd = StoreDataCmdExecutor()
    # 类型实现
    __impl = {
        "raf": _raf,
        "sd": _sd
    }

    @staticmethod
    def get_instance(impl):
        return CmdManager.__impl.get(impl)


