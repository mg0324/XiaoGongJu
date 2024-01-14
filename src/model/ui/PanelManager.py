# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : PanelManager
# @Time   : 2024/1/14 13:54
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.ui.JSONPanelStrategy import JSONPanelStrategy
from src.model.ui.RoundPanelStrategy import RoundPanelStrategy


class PanelManager:
    roundPanelStrategy = RoundPanelStrategy()
    jsonPanelStrategy = JSONPanelStrategy()

    # 类型实现
    __impl = {
        CmdEnum.ROUND.value.get("value"): roundPanelStrategy,
        0: roundPanelStrategy,
        CmdEnum.JSON.value.get("value"): jsonPanelStrategy,
        1: jsonPanelStrategy
    }

    @staticmethod
    def get_instance(impl):
        return PanelManager.__impl.get(impl)
