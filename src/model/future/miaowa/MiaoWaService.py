# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : RoundService
# @Time   : 2024/1/14 13:23
# @Author : mango
import json

from src.model.Service import Service
from src.model.future.miaowa.compontent.Browser import Browser
from src.model.future.miaowa.compontent.Config import Config
from src.model.future.miaowa.compontent.Context import Context
from src.model.future.miaowa.compontent.GetTime import GetTime
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.compontent.Store import Store
from src.model.future.miaowa.compontent.cmd.CmdManager import CmdManager
from src.util.WxUtil import WxUtil


class MiaoWaService(Service):

    def __init__(self, context: Context):
        # 创建浏览器
        self.browser = Browser(context)
        # 创建店
        self.store = Store(context.getStoreCode())
        # 参数上下文
        self.context = context
        # 配置
        self.config = Config()

    def getResult(self):
        pass

    @GetTime("主工作")
    def startWorking(self, cmdName):
        cmdExecutor = CmdManager.get_instance(cmdName)
        if cmdExecutor:
            LogUtil.debug("执行命令:" + cmdName)
            cmdExecutor.execute(self)

    @GetTime("登录到店")
    def do_login(self):
        # 没有加载cookie则加载
        if not self.store.is_login():
            cookies_path = self.store.get_cookies_path(self.context)
            # 找到最小需要的cookies，加快登录cookie的操作
            needs = ["aep_common_f", "xman_t"]
            # 设置cookies跳过登录
            with open(cookies_path) as f:
                list_cookies = json.loads(f.read())
            for cookie in list_cookies:
                if cookie["name"] in needs:
                    del cookie['sameSite']
                    self.browser.add_cookie(cookie)
            # 设置登录状态为True
            self.store.set_login(True)
        pass

    # 登录到后端首页
    @GetTime("登录到订单首页")
    def login_to_home(self):
        # 尝试到首页
        self.browser.get(self.store.home_url)
        # 登录
        self.do_login()
        pass

    def shutDown(self):
        self.browser.switch_window(0)
        self.browser.close()
        pass