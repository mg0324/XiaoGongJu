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

        choiceIsHeadlessChoices = [u"是", u"否"]
        self.choiceIsHeadless = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceIsHeadlessChoices,
                                          0)
        self.choiceIsHeadless.SetSelection(0)
        wSizer5.Add(self.choiceIsHeadless, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText15 = wx.StaticText(self, wx.ID_ANY, u"配置目录：", wx.DefaultPosition, wx.Size(-1, -1),
                                            wx.ALIGN_RIGHT)
        self.m_staticText15.Wrap(-1)

        self.m_staticText15.SetToolTip(u"xxx")

        wSizer5.Add(self.m_staticText15, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.inputConfig = wx.TextCtrl(self, wx.ID_ANY, u"/Users/mango/.xgj/miaowa", wx.DefaultPosition,
                                       wx.Size(200, -1), 0)
        wSizer5.Add(self.inputConfig, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer5.Add(self.m_button12, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer12.Add(wSizer5, 0, wx.EXPAND, 5)

        wSizer6 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText16 = wx.StaticText(self, wx.ID_ANY, u"当前店铺：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)

        wSizer6.Add(self.m_staticText16, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        choiceStoreChoices = []
        self.choiceStore = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceStoreChoices, 0)
        self.choiceStore.SetSelection(0)
        wSizer6.Add(self.choiceStore, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"子功能：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        wSizer6.Add(self.m_staticText21, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.radioRaf = wx.RadioButton(self, wx.ID_ANY, u"RAF", wx.DefaultPosition, wx.Size(200, -1), 0)
        self.radioRaf.SetValue(True)
        self.radioRaf.SetToolTip(u"评价并且发生Follow消息")

        wSizer6.Add(self.radioRaf, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_staticText161 = wx.StaticText(self, wx.ID_ANY, u"当前页：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText161.Wrap(-1)

        wSizer6.Add(self.m_staticText161, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        choicePageChoices = [u"1"]
        self.choicePage = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePageChoices, 0)
        self.choicePage.SetSelection(0)
        wSizer6.Add(self.choicePage, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        bSizer12.Add(wSizer6, 0, wx.EXPAND, 5)

        sbSizer51 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"日志"), wx.VERTICAL)

        self.long_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sbSizer51.Add(self.long_text, 1, wx.EXPAND | wx.ALL, 0)

        bSizer12.Add(sbSizer51, 20, wx.EXPAND, 5)

        wSizer8 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.btnMain = wx.Button(self, wx.ID_ANY, u"开始执行", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer8.Add(self.btnMain, 0, wx.ALL, 5)

        bSizer12.Add(wSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        # Connect Events
        self.btnMain.Bind(wx.EVT_BUTTON, self.doExecute)
        self.init()

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def doExecute(self, event):
        event.Skip()
