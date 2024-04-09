# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : JSONPanelImpl
# @Time   : 2024/4/8 23:30
# @Author : mango
from src.model.future.json.JSONPanel import JSONPanel
from src.model.future.json.JSONService import JSONService
from src.util.WxUtil import WxUtil
from src.vo.JSONVO import JSONVO


class JSONPanelImpl(JSONPanel):

    def doFormat(self, event):
        intputStr = self.richTextInput.GetValue()
        result = JSONService().getResult(JSONVO(intputStr))
        WxUtil.writeResult2RichText(self.richTextOutput, result)
