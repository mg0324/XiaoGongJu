# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONPanelImpl
# @Time   : 2024/4/8 23:30
# @Author : mango
from src.model.future.json.JSONPanel import JSONPanel


class JSONPanelImpl(JSONPanel):

    def doFormat(self, event):
        event.Skip()
