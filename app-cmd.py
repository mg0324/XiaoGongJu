# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : __init__.py
# @Time   : 2023/12/31 11:01
# @Author : mango
import sys
from src.util.LogUtil import LogUtil
from src.config.Config import Config
from src.util.showtime import showtime
from src.view.Argument import Argument
from src.model.CmdManager import CmdManager


class App:
    # 配置
    config = None
    # 命令行参数
    argument = None

    def __init__(self, name):
        self.name = name
        self.config = Config()
        self.argument = Argument(self.name)
        # 设置日志级别
        LogUtil.set_level(self.argument.get_args().log_level)
        LogUtil.debug("[XiaoGongJu]参数集：" + str(self.argument.get_args()))

        pass

    @showtime(stage="主工作")
    def run(self):
        if len(sys.argv) == 1:
            self.argument.get_parser().print_help()
        elif len(sys.argv) > 1:
            # 根据子命令分流执行 找到子命令
            cmdName = self.find_sub_cmd()
            cmdStrategy = CmdManager.get_instance(cmdName)
            if cmdStrategy:
                LogUtil.debug("执行命令:" + cmdName)
                cmdStrategy.execute(self)
            else:
                raise RuntimeWarning("不支持的子命令[{}]", cmdName)
        pass

    # 找到子命令
    @staticmethod
    def find_sub_cmd():
        index = 1
        while True:
            cmd = sys.argv[index]
            if not cmd.startswith("-"):
                return cmd
            index = index + 1


if __name__ == '__main__':
    app = App("XiaoGongJu")
    #sys.argv = ['app-cmd.py', 'round']
    app.run()
