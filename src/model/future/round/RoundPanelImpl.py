# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundPanelImpl
# @Time   : 2024/4/8 23:37
# @Author : mango
from src.config.TemplateConfig import TemplateConfig
from src.model.future.round.RoundPanel import RoundPanel


class RoundPanelImpl(RoundPanel):

    def init(self):
        self.changeTemplate(None)

    def changeTemplate(self, event):
        template = TemplateConfig.getConfig().get(self.templateChoice.GetStringSelection())
        self.templateDesc.SetLabel(template.get("desc"))
        self.inputLeft.SetValue(template.get("left"))
        self.inputRight.SetValue(template.get("right"))
        self.inputSeparator.SetValue(template.get("separator"))
