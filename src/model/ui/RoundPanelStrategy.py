# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundPanelStrategy
# @Time   : 2024/1/14 13:56
# @Author : mango
from src.config.CmdTypeEnum import CmdTypeEnum
from src.model.RoundService import RoundService
from src.model.ui.PanelStrategy import PanelStrategy
from src.util.WxUtil import WxUtil
from src.view.panel.RoundPanel import RoundPanel
from src.vo.RoundVO import RoundVO


class RoundPanelStrategy(PanelStrategy):

    def __init__(self):
        self.panel = None
        self.service = RoundService()

    def getPanel(self):
        return self.panel

    def handlePanel(self, app):
        if self.panel:
            app.auiNotebook.SetSelection(0)
        else:
            self.panel = RoundPanel(app.auiNotebook)
            app.auiNotebook.InsertPage(0, self.panel, u"round", True)
        pass

    def format(self, app):
        separator = self.panel.inputSeparator.GetValue()
        separator = separator.replace("\\n", "\n")
        left = self.panel.inputLeft.GetValue()
        right = self.panel.inputRight.GetValue()
        lines = self.panel.richTextInput.GetValue().split("\n")
        roundVO = RoundVO(left, right, separator, lines)
        result = self.service.getResult(roundVO)
        WxUtil.writeResult2RichText(self.panel.richTextOutput, result)

    def type(self):
        return CmdTypeEnum.FORMATE

