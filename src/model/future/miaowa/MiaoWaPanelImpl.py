# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : MiaoWaPanelImpl
# @Time   : 2024/4/13 22:13
# @Author : mango
import os
import traceback
import threading
import logging

from src.model.future.miaowa.MiaoWaPanel import MiaoWaPanel
from src.model.future.miaowa.MiaoWaService import MiaoWaService
from src.model.future.miaowa.compontent.Context import Context
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.LogHandler import WxTextCtrlHandler

_store = {
    "运动店": {
        "code": "sport"
    },
    "运动店2": {
        "code": "sport2"
    }
}


def getStoreList():
    return list(_store)


def getDefaultConfigDir():
    return os.path.expanduser("~") + "/.xgj/miaoWa"


class MiaoWaPanelImpl(MiaoWaPanel):
    service = None

    def init(self):
        self.choiceStore.Set(getStoreList())
        self.choicePage.Set([str(x) for x in range(1, 10)])
        self.inputConfig.SetValue(getDefaultConfigDir())
        self.service = None
        self.setup_logging()


    def setup_logging(self):
        """
        Set up logging from configuration file and initialize wxHandler.
        """
        # 先加载配置
        logging.config.fileConfig('logging.conf')
        # 使用配置文件中的Logger
        logger = logging.getLogger('my_logger')

        # 初始化并设置WxTextCtrlHandler
        for handler in logger.handlers:
            if isinstance(handler, WxTextCtrlHandler):
                handler.text_ctrl = self.long_text

    def doExecute(self, event):
        storeLabel = self.choiceStore.GetStringSelection()
        storeCode = _store[storeLabel]["code"]
        page = self.choicePage.GetStringSelection()
        isSd = self.radioSd.GetValue()
        configDir = self.inputConfig.GetValue()
        choiceIsHeadless = self.choiceIsHeadless.GetStringSelection()
        subCmd = 'raf'
        if isSd:
            subCmd = 'sd'
        LogUtil.info(f'storeLabel:{storeLabel},storeCode:{storeCode},page:{page},subCmd:{subCmd},configDir:{configDir},choiceIsHeadless:{choiceIsHeadless}')
        self.service = MiaoWaService(context=Context(store=storeCode, page=page,
                                                     configDir=configDir, isHeadless=choiceIsHeadless))
        try:
            # 先清理
            self.long_text.Clear()
            # 创建主工作线程
            threadMain = threading.Thread(target=self.service.startWorking, args=(subCmd,))
            # 开启任务
            threadMain.start()
        except Exception as e:
            traceback.print_exc()
            msg = "程序出错，{} \n".format(e)
            self.long_text.AppendText(msg)
        pass
