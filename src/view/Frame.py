# -*- coding: utf-8 -*-
from abc import abstractmethod, ABC

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


###########################################################################
## Class Frame
###########################################################################

class Frame(wx.Frame):

    def __init__(self, parent, *args, **kw):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=self.title(), pos=wx.DefaultPosition,
                          size=self.getSize(),
                          style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE | wx.MINIMIZE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.menuBar = wx.MenuBar(0)
        self.menuFile = wx.Menu()
        self.menuAbout = wx.MenuItem(self.menuFile, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuFile.Append(self.menuAbout)

        self.menuExit = wx.MenuItem(self.menuFile, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        self.menuFile.Append(self.menuExit)

        self.menuBar.Append(self.menuFile, u"文件")

        self.SetMenuBar(self.menuBar)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText20 = wx.StaticText(self, wx.ID_ANY, u"特性", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)

        bSizer6.Add(self.m_staticText20, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        cmdChoiceChoices = self.getChoices()
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

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.menuAbout.GetId())
        self.Bind(wx.EVT_MENU, self.onExit, id=self.menuExit.GetId())
        self.cmdChoice.Bind(wx.EVT_CHOICE, self.changeCmd)

        self.init()

    def __del__(self):
        pass

    @abstractmethod
    def getChoices(self):
        pass

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    # Virtual event handlers, override them in your derived class
    def onAbout(self, event):
        event.Skip()

    def onExit(self, event):
        event.Skip()

    def changeCmd(self, event):
        event.Skip()

    def init(self):
        pass


