# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundPanelImpl
# @Time   : 2024/4/8 23:37
# @Author : mango
from src.config.TemplateConfig import TemplateConfig
from src.model.future.round.RoundPanel import RoundPanel
from src.model.future.round.RoundService import RoundService
from src.util.WxUtil import WxUtil
from src.vo.RoundVO import RoundVO


class RoundPanelImpl(RoundPanel):

    def init(self):
        self.changeTemplate(None)

    def changeTemplate(self, event):
        template = TemplateConfig.getConfig().get(self.templateChoice.GetStringSelection())
        self.templateDesc.SetLabel(template.get("desc"))
        self.inputLeft.SetValue(template.get("left"))
        self.inputRight.SetValue(template.get("right"))
        self.inputSeparator.SetValue(template.get("separator"))

    def doFormat(self, event):
        separator = self.inputSeparator.GetValue()
        separator = separator.replace("\\n", "\n")
        left = self.inputLeft.GetValue()
        right = self.inputRight.GetValue()
        lines = self.richTextInput.GetValue().split("\n")
        roundVO = RoundVO(left, right, separator, lines)
        result = RoundService().getResult(roundVO)
        WxUtil.writeResult2RichText(self.richTextOutput, result)
