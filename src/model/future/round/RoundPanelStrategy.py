# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundPanelStrategy
# @Time   : 2024/1/14 13:56
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.future.round.RoundPanelImpl import RoundPanelImpl
from src.model.future.round.RoundService import RoundService
from src.model.ui.PanelStrategy import PanelStrategy
from src.util.WxUtil import WxUtil
from src.vo.RoundVO import RoundVO


class RoundPanelStrategy(PanelStrategy):

    def __init__(self):
        self.panel = None
        self.service = RoundService()

    def createPanel(self, app):
        self.panel = RoundPanelImpl(app.auiNotebook)
        return self.panel

    def getPanel(self):
        return self.panel

    def type(self):
        return CmdEnum.ROUND

