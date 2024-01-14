# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : CmdStrategy
# @Time   : 2023/12/31 13:51
# @Author : mango
from abc import ABC, abstractmethod


# 命令策略
class CmdStrategy(ABC):
    # 参数
    __args = None

    # 执行命令接口
    @abstractmethod
    def execute(self, app):
        pass

    # 注册子命令
    @abstractmethod
    def register(self, subparsers):
        pass

    @abstractmethod
    def type(self):
        pass
