# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : WxUtil
# @Time   : 2024/1/14 14:36
# @Author : mango
import wx.richtext as rt


class WxUtil:

    @staticmethod
    def writeResult2RichText(richText, result):
        attr = rt.RichTextAttr()
        richText.BeginStyle(attr)
        richText.Clear()
        richText.WriteText(result)
        richText.EndAllStyles()

    @staticmethod
    def appendResult2RichText(richText, result):
        attr = rt.RichTextAttr()
        richText.BeginStyle(attr)
        richText.AppendText(result)
        richText.EndAllStyles()
