# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext


###########################################################################
## Class MiaoWaPanel
###########################################################################

class MiaoWaPanel(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(885, 603), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        wSizer2 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用小工具之妙娃小帮手！", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        wSizer2.Add(self.m_staticText13, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText14 = wx.StaticText(self, wx.ID_ANY, u"V1.0.0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        wSizer2.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer12.Add(wSizer2, 0, wx.EXPAND, 5)

        wSizer5 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText17 = wx.StaticText(self, wx.ID_ANY, u"是否开启无头浏览器模式运行：", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)

        wSizer5.Add(self.m_staticText17, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice4Choices = [u"是", u"否"]
        self.m_choice4 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0)
        self.m_choice4.SetSelection(0)
        wSizer5.Add(self.m_choice4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"配置目录：", wx.DefaultPosition, wx.Size(-1, -1),
                                            wx.ALIGN_RIGHT)
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetToolTip(u"xxx")

        wSizer5.Add(self.m_staticText15, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, u"/Users/mango/.xgj/miaowa", wx.DefaultPosition,
                                       wx.Size(200, -1), 0)
        wSizer5.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer5.Add(self.m_button12, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer12.Add(wSizer5, 0, wx.EXPAND, 5)

        wSizer6 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"当前店铺：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        wSizer6.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice3Choices = self.getStoreList()
        self.m_choice3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        wSizer6.Add(self.m_choice3, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"子功能：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        wSizer6.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_radioBtn4 = wx.RadioButton(self, wx.ID_ANY, u"RAF", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.m_radioBtn4.SetValue(True)
        self.m_radioBtn4.SetToolTip(u"评价并且发生Follow消息")

        wSizer6.Add(self.m_radioBtn4, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText161 = wx.StaticText(self, wx.ID_ANY, u"当前页：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)

        wSizer6.Add(self.m_staticText161, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        m_choice31Choices = [str(i) for i in range(1, 10)]
        self.m_choice31 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice31Choices, 0)
        self.m_choice31.SetSelection(0)
        wSizer6.Add(self.m_choice31, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer12.Add(wSizer6, 0, wx.EXPAND, 5)

        sbSizer51 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"日志"), wx.VERTICAL)

        self.richTextOutput = wx.richtext.RichTextCtrl(sbSizer51.GetStaticBox(), wx.ID_ANY, u"123", wx.DefaultPosition,
                                                       wx.DefaultSize,
                                                       0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        sbSizer51.Add(self.richTextOutput, 1, wx.EXPAND | wx.ALL, 0)

        bSizer12.Add(sbSizer51, 20, wx.EXPAND, 5)

        wSizer8 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"开始执行", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer8.Add(self.m_button13, 0, wx.ALL, 5)

        bSizer12.Add(wSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.init()

    def __del__(self):
        pass

    def init(self):
        pass

    def getStoreList(self):
        pass
