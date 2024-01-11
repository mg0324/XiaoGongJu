# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project: XiaoGongJu
# @File   : app-wx
# @Time   : 2024/1/3 23:43
# @Author : mango
import wx

from src.view.Frame import Frame


def main():
    app = wx.App()
    ex = Frame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

