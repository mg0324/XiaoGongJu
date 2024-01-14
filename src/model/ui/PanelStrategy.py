# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : PanelStrategy
# @Time   : 2024/1/14 13:52
# @Author : mango
from abc import ABC, abstractmethod


# panel策略
class PanelStrategy(ABC):

    @abstractmethod
    def getPanel(self):
        pass

    @abstractmethod
    def handlePanel(self, app):
        pass

    @abstractmethod
    def format(self, app):
        pass

    @abstractmethod
    def type(self):
        pass
