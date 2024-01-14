# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONPanelStrategy
# @Time   : 2024/1/14 13:56
# @Author : mango
from src.config.CmdTypeEnum import CmdTypeEnum
from src.model.JSONService import JSONService
from src.model.ui.PanelStrategy import PanelStrategy
from src.util.WxUtil import WxUtil
from src.view.panel.JSONPanel import JSONPanel
from src.vo.JSONVO import JSONVO


class JSONPanelStrategy(PanelStrategy):

    def __init__(self):
        self.panel = None
        self.service = JSONService()

    def getPanel(self):
        return self.panel

    def handlePanel(self, app):
        if self.panel:
            app.auiNotebook.SetSelection(1)
        else:
            self.panel = JSONPanel(app.auiNotebook)
            app.auiNotebook.InsertPage(1, self.panel, u"json", True)

    def format(self, app):
        intputStr = self.panel.richTextInput.GetValue()
        result = self.service.getResult(JSONVO(intputStr))
        WxUtil.writeResult2RichText(self.panel.richTextOutput, result)

    def type(self):
        return CmdTypeEnum.FORMATE

