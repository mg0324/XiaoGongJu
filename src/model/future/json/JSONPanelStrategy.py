# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONPanelStrategy
# @Time   : 2024/1/14 13:56
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.future.json.JSONPanelImpl import JSONPanelImpl
from src.model.future.json.JSONService import JSONService
from src.model.ui.PanelStrategy import PanelStrategy
from src.util.WxUtil import WxUtil
from src.model.future.json.JSONPanel import JSONPanel
from src.vo.JSONVO import JSONVO


class JSONPanelStrategy(PanelStrategy):

    def __init__(self):
        self.panel = None
        self.service = JSONService()

    def createPanel(self, app):
        self.panel = JSONPanelImpl(app.auiNotebook)
        return self.panel

    def getPanel(self):
        return self.panel

    def type(self):
        return CmdEnum.JSON

