# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : CmdManager
# @Time   : 2023/12/31 11:53
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.cmd.JSONCmdStrategy import JSONCmdStrategy
from src.model.cmd.RoundCmdStrategy import RoundCmdStrategy


# cmd管理器
class CmdManager:
    # 类型实现
    __impl = {
        CmdEnum.ROUND.value.get("value"): RoundCmdStrategy(),
        CmdEnum.JSON.value.get("value"): JSONCmdStrategy()
    }

    @staticmethod
    def get_instance(impl):
        return CmdManager.__impl.get(impl)

    # 注册命令
    @staticmethod
    def register(parser):
        subparsers = parser.add_subparsers(help='子命令说明')
        for executor in CmdManager.__impl.values():
            executor.register(subparsers)


if __name__ == '__main__':
    CmdManager.register()
