# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : FrameModel
# @Time   : 2024/1/14 14:05
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.ui.PanelManager import PanelManager
from src.view.Frame import Frame


class FrameModel(Frame):

    def init(self):
        self.changeCmd(None)

    def changeCmd(self, event):
        item = CmdEnum.getItemByValue(self.cmdChoice.GetStringSelection())
        self.cmdDesc.SetValue(item.value.get("desc"))
        panelStrategy = PanelManager.get_instance(item.value.get("value"))
        if panelStrategy:
            panelStrategy.handlePanel(self)

    def doFormat(self, event):
        index = self.auiNotebook.GetSelection()
        panelStrategy = PanelManager.get_instance(index)
        if panelStrategy:
            panelStrategy.format(self)
