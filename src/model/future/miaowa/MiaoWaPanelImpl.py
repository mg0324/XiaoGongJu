# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : MiaoWaPanelImpl
# @Time   : 2024/4/13 22:13
# @Author : mango
import os
import platform
import subprocess
import traceback
import threading

from src.model.future.miaowa.MiaoWaPanel import MiaoWaPanel
from src.model.future.miaowa.MiaoWaService import MiaoWaService
from src.model.future.miaowa.compontent.Config import Config
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


class MiaoWaPanelImpl(MiaoWaPanel):
    service = None

    def init(self):
        self.choiceStore.Set(getStoreList())
        self.choicePage.Set([str(x) for x in range(1, 10)])
        self.inputConfig.SetValue(Config.getDefaultConfigDir())
        self.textVersion.SetLabel(f"V{Config.getMiaoWaVersion()}")
        self.service = None
        self.setup_logging()

    def choseSd(self, event):
        self.choicePage.Hide()
        self.textCurPage.Hide()

    def choseRaf(self, event):
        self.choicePage.Show()
        self.textCurPage.Show()


    def setup_logging(self):
        # 获取logger
        logger = LogUtil.getLogger()
        # 初始化并设置WxTextCtrlHandler
        for handler in logger.handlers:
            if isinstance(handler, WxTextCtrlHandler):
                handler.text_ctrl = self.richTextOutput

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
            self.richTextOutput.Clear()
            # 创建主工作线程
            threadMain = threading.Thread(target=self.service.startWorking, args=(subCmd,))
            # 开启任务
            threadMain.start()
        except Exception as e:
            traceback.print_exc()
            msg = "程序出错，{} \n".format(e)
            self.richTextOutput.AppendText(msg)
        pass


    def openDir(self, event):
        path = Config.getDefaultConfigDir()
        # 确保路径存在
        if not os.path.isdir(path):
            raise NotADirectoryError(f"{path} 不是一个有效的目录")

        # 获取当前操作系统类型
        system = platform.system()

        try:
            if system == "Windows":
                os.startfile(path)
            elif system == "Darwin":  # macOS
                subprocess.Popen(["open", path])
            elif system == "Linux":
                subprocess.Popen(["xdg-open", path])
            else:
                raise NotImplementedError(f"不支持的操作系统: {system}")
        except Exception as e:
            print(f"打开目录时出错: {e}")

    def stopTask(self, event):
        pass