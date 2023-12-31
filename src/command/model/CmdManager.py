# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : CmdManager
# @Time   : 2023/12/31 11:53
# @Author : mango
from src.command.model.RoundCmdStrategy import RoundCmdStrategy


# cmd管理器
class CmdManager:
    # 类型实现
    __impl = {
        "round": RoundCmdStrategy()
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
