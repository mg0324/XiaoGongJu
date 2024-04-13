# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : PanelStrategy
# @Time   : 2024/1/14 13:52
# @Author : mango
from abc import ABC, abstractmethod


# panel策略
class PanelStrategy(ABC):
    __panelMap = {}

    @abstractmethod
    def getPanel(self):
        pass

    @abstractmethod
    def createPanel(self, app):
        pass

    def handlePanel(self, app, panelKey):
        if self.getPanel():
            pageIndex = app.auiNotebook.GetPageIndex(self.getPanel())
            app.auiNotebook.SetSelection(pageIndex)
        else:
            panel = self.createPanel(app)
            app.auiNotebook.AddPage(panel, panelKey, True)
        return self.getPanel()

    @abstractmethod
    def type(self):
        pass
