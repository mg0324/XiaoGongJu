# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : PanelManager
# @Time   : 2024/1/14 13:54
# @Author : mango
from src.config.CmdEnum import CmdEnum
from src.model.future.json.JSONPanelStrategy import JSONPanelStrategy
from src.model.future.round.RoundPanelStrategy import RoundPanelStrategy


class PanelManager:

    # 类型实现
    __impl = {
        CmdEnum.ROUND.value.get("value"): RoundPanelStrategy(),
        CmdEnum.JSON.value.get("value"): JSONPanelStrategy(),
    }

    @staticmethod
    def get_instance(impl):
        return PanelManager.__impl.get(impl)
