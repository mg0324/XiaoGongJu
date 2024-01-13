# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

from src.config.CmdEnum import CmdEnum
from src.view.JSONPanel import JSONPanel
from src.view.RoundPanel import RoundPanel


###########################################################################
## Class Frame
###########################################################################

class Frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"小工具", pos=wx.DefaultPosition, size=wx.Size(1000, 700),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE | wx.MINIMIZE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.menuBar = wx.MenuBar(0)
        self.menuFile = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.menuFile, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuFile.Append(self.m_menuItem1)

        self.menuBar.Append(self.menuFile, u"文件")

        self.menuAbout = wx.Menu()
        self.menuBar.Append(self.menuAbout, u"关于")

        self.SetMenuBar(self.menuBar)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"命令", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)

        bSizer6.Add(self.m_staticText20, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cmdChoiceChoices = [u"round", u"json"]
        self.cmdChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cmdChoiceChoices, 0)
        self.cmdChoice.SetSelection(0)
        bSizer6.Add(self.cmdChoice, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer5.Add(bSizer6, 1, wx.EXPAND, 1)

        self.cmdDesc = wx.TextCtrl(self, wx.ID_ANY, u"说明", wx.DefaultPosition, wx.Size(-1, -1),
                                   wx.TE_CHARWRAP | wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_NOHIDESEL | wx.TE_NO_VSCROLL | wx.TE_READONLY | wx.TE_WORDWRAP)
        self.cmdDesc.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVEBORDER))

        bSizer5.Add(self.cmdDesc, 22, wx.ALL | wx.EXPAND, 1)

        bSizer10.Add(bSizer5, 0, wx.EXPAND, 0)

        self.auiNotebook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.aui.AUI_NB_DEFAULT_STYLE)

        bSizer10.Add(self.auiNotebook, 1, wx.EXPAND | wx.ALL, 5)

        bSizer3.Add(bSizer10, 1, wx.EXPAND, 0)

        self.m_button31 = wx.Button(self, wx.ID_ANY, u"格式化", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button31, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.cmdChoice.Bind(wx.EVT_CHOICE, self.changeCmd)

        self.init()

    def __del__(self):
        pass

    def init(self):
        self.changeCmd(None)

    def changeCmd(self, event):
        item = CmdEnum.getItemByValue(self.cmdChoice.GetStringSelection())
        self.cmdDesc.SetValue(item.value.get("desc"))
        if item == CmdEnum.ROUND:
            panel = RoundPanel(self.auiNotebook)
            self.auiNotebook.AddPage(panel, u"round", False, 1)
        elif item == CmdEnum.JSON:
            panel = JSONPanel(self.auiNotebook)
            self.auiNotebook.AddPage(panel, u"json", True, 2)
