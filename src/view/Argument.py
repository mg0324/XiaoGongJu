# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : Argument
# @Time   : 2023/12/31 11:52
# @Author : mango

import argparse
from src.model.cmd.CmdManager import CmdManager


# 命令行参数类
class Argument:
    # 参数
    __args = None
    # 主解析器
    __parser = None
    # cmd名称
    __name = None

    # 版本号
    def get_version(self):
        return self.__name + " 1.0.0"

    # 初始化主参数
    def init_main_args(self, parser):
        parser.add_argument('-v', '--version',
                            action="version",
                            version=self.get_version(),
                            help="查看版本号")

        parser.add_argument('-ll', '--log_level',
                            default="warning",
                            type=str,
                            metavar="",
                            required=False,
                            help="日志级别，warning-告警，debug-调试，info-信息，error-错误；默认%(default)s")

        pass

    def __init__(self, name):
        self.__name = name
        description = "欢迎使用 " + self.get_version()
        usage = "python3 app-cmd.py [cmd]"
        parser = argparse.ArgumentParser(usage=usage,
                                         prog=self.__name,
                                         description=description,
                                         allow_abbrev=False)
        # 初始化参数
        self.init_main_args(parser)
        # 注册子命令
        CmdManager.register(parser)
        self.__args = parser.parse_args()
        self.__parser = parser
        pass

    # 获取参数
    def get_args(self):
        return self.__args

    def get_parser(self):
        return self.__parser
