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
## Class JSONPanel
###########################################################################

class JSONPanel(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"输入"), wx.VERTICAL)

        self.richTextInput = wx.richtext.RichTextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, u"input", wx.DefaultPosition,
                                                      wx.DefaultSize,
                                                      0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        sbSizer4.Add(self.richTextInput, 1, wx.EXPAND | wx.ALL, 0)

        bSizer17.Add(sbSizer4, 10, wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"输出"), wx.VERTICAL)

        self.richTextOutput = wx.richtext.RichTextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, u"output",
                                                       wx.DefaultPosition, wx.DefaultSize,
                                                       0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        sbSizer5.Add(self.richTextOutput, 1, wx.EXPAND | wx.ALL, 0)

        bSizer17.Add(sbSizer5, 10, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.btnFormat = wx.Button(self, wx.ID_ANY, u"格式化", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.btnFormat, 0, wx.ALL, 5)

        bSizer17.Add(bSizer8, 1, wx.EXPAND, 1)

        self.SetSizer(bSizer17)
        self.Layout()

        # Connect Events
        self.btnFormat.Bind(wx.EVT_BUTTON, self.doFormat)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def doFormat(self, event):
        event.Skip()
