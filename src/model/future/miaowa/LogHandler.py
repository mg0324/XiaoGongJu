# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : logging-handler
# @Time   : 2024/6/16 15:36
# @Author : mango
import logging
import wx


# wx logger handler
class WxTextCtrlHandler(logging.Handler):
    """
    A custom logging handler that sends logs to a wx.TextCtrl.
    """
    def __init__(self, text_ctrl):
        super().__init__()
        self.text_ctrl = text_ctrl

    def emit(self, record):
        msg = self.format(record)
        wx.CallAfter(self.text_ctrl.AppendText, msg + '\n')
        self.flush()
