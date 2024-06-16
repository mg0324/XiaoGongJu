# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : MiaoWaPanelImpl
# @Time   : 2024/4/13 22:13
# @Author : mango
import os
import traceback

from src.model.future.miaowa.MiaoWaPanel import MiaoWaPanel
from src.model.future.miaowa.MiaoWaService import MiaoWaService
from src.model.future.miaowa.compontent.Context import Context
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.util.WxUtil import WxUtil

_store = {
    "运动店": {
        "code": "sport"
    }
}


def getStoreList():
    return [u"运动店"]


def getDefaultConfigDir():
    return os.path.expanduser("~") + "/.xgj/miaoWa"


class MiaoWaPanelImpl(MiaoWaPanel):
    service = None

    def init(self):
        self.choiceStore.Set(getStoreList())
        self.choicePage.Set([str(x) for x in range(1, 10)])
        self.inputConfig.SetValue(getDefaultConfigDir())
        self.service = None

    def doExecute(self, event):
        storeLabel = self.choiceStore.GetStringSelection()
        storeCode = _store[storeLabel]["code"]
        page = self.choicePage.GetStringSelection()
        isRaf = self.radioRaf.GetValue()
        configDir = self.inputConfig.GetValue()
        choiceIsHeadless = self.choiceIsHeadless.GetStringSelection()
        LogUtil.info(f'storeLabel:{storeLabel},storeCode:{storeCode},page:{page},isRaf:{isRaf},configDir:{configDir},choiceIsHeadless:{choiceIsHeadless}')
        self.service = MiaoWaService(context=Context(store=storeCode, page=page,
                                                     configDir=configDir, isHeadless=choiceIsHeadless))
        try:
            self.service.startWorking("raf")
            self.service.shutDown()
        except Exception as e:
            traceback.print_exc()
            WxUtil.writeResult2RichText(self.richTextOutput, "程序出错，{}".format(e))
        pass
