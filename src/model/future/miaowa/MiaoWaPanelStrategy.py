# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : MiaoWaPanelStrategy
# @Time   : 2024/4/13 13:56
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.future.miaowa.MiaoWaPanelImpl import MiaoWaPanelImpl
from src.model.future.PanelStrategy import PanelStrategy


class MiaoWaService:
    pass


class MiaoWaPanelStrategy(PanelStrategy):

    def __init__(self):
        self.panel = None
        self.service = MiaoWaService()

    def createPanel(self, app):
        self.panel = MiaoWaPanelImpl(app.auiNotebook)
        return self.panel

    def getPanel(self):
        return self.panel

    def type(self):
        return CmdEnum.ROUND

