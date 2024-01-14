# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : app-wx
# @Time   : 2024/1/3 23:43
# @Author : mango
import wx

from src.model.FrameModel import FrameModel


def main():
    app = wx.App()
    ex = FrameModel(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

