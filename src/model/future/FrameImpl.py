# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : FrameModel
# @Time   : 2024/1/14 14:05
# @Author : mango
import wx
import wx.adv

from src.config.CmdEnum import CmdEnum
from src.config.Config import Config
from src.model.future.PanelManager import PanelManager
from src.view.Frame import Frame


class FrameImpl(Frame):

    def init(self):
        self.changeCmd(None)

    def getChoices(self):
        return CmdEnum.getCmdList()

    def title(self):
        return Config.about["name"]

    def getSize(self):
        return wx.Size(Config.windowSize[0], Config.windowSize[1])

    def changeCmd(self, event):
        item = CmdEnum.getItemByValue(self.cmdChoice.GetStringSelection())
        self.cmdDesc.SetValue(item.value.get("desc"))
        name = item.value.get("value")
        panelStrategy = PanelManager.get_instance(name)
        if panelStrategy:
            panelStrategy.handlePanel(self, name)

    def onAbout(self, event):
        info = wx.adv.AboutDialogInfo()
        # info.SetIcon(wx.Icon('images/logo.png', wx.BITMAP_TYPE_PNG))
        info.SetName(Config.about["name"])
        info.SetVersion(Config.about["version"])
        info.SetDescription(Config.about["desc"])
        info.SetCopyright(Config.about["copyright"])
        # info.SetWebSite('http://www.zetcode.com')
        wx.adv.AboutBox(info)

    def onExit(self, event):
        self.Close()
