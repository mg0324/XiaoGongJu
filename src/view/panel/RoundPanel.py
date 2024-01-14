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

from src.config.TemplateConfig import TemplateConfig


###########################################################################
## Class RoundPanel
###########################################################################

class RoundPanel(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.TAB_TRAVERSAL,
                 name=wx.EmptyString):
        wx.Panel.__init__(self, parent, id=id, pos=pos, size=size, style=style, name=name)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        wSizerTemplate = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.templateLabel = wx.StaticText(self, wx.ID_ANY, u"模板", wx.DefaultPosition, wx.DefaultSize, 0)
        self.templateLabel.Wrap(-1)

        wSizerTemplate.Add(self.templateLabel, 0, wx.ALIGN_CENTER | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        templateChoiceChoices = [u"default", u"result.add"]
        self.templateChoice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, templateChoiceChoices, 0)
        self.templateChoice.SetSelection(0)
        wSizerTemplate.Add(self.templateChoice, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.templateDesc = wx.StaticText(self, wx.ID_ANY, u"说明", wx.DefaultPosition, wx.DefaultSize, 0)
        self.templateDesc.Wrap(-1)

        wSizerTemplate.Add(self.templateDesc, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer7.Add(wSizerTemplate, 0, wx.EXPAND, 0)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.textLeft = wx.StaticText(self, wx.ID_ANY, u"左侧", wx.DefaultPosition, wx.DefaultSize, 0)
        self.textLeft.Wrap(-1)

        bSizer11.Add(self.textLeft, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.inputLeft = wx.TextCtrl(self, wx.ID_ANY, u"'", wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer11.Add(self.inputLeft, 0, wx.ALL | wx.EXPAND, 5)

        self.rightText = wx.StaticText(self, wx.ID_ANY, u"右侧", wx.DefaultPosition, wx.DefaultSize, 0)
        self.rightText.Wrap(-1)

        bSizer11.Add(self.rightText, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.inputRight = wx.TextCtrl(self, wx.ID_ANY, u"'", wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer11.Add(self.inputRight, 0, wx.ALL, 5)

        self.textSeparator = wx.StaticText(self, wx.ID_ANY, u"分隔符", wx.DefaultPosition, wx.DefaultSize, 0)
        self.textSeparator.Wrap(-1)

        bSizer11.Add(self.textSeparator, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.inputSeparator = wx.TextCtrl(self, wx.ID_ANY, u",\\n", wx.DefaultPosition, wx.Size(100, -1), 0)
        bSizer11.Add(self.inputSeparator, 0, wx.ALL, 5)

        bSizer7.Add(bSizer11, 1, wx.EXPAND, 5)

        sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"输入文件input.txt"), wx.VERTICAL)

        self.richTextInput = wx.richtext.RichTextCtrl(sbSizer4.GetStaticBox(), wx.ID_ANY, u"input", wx.DefaultPosition,
                                                      wx.DefaultSize,
                                                      0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        sbSizer4.Add(self.richTextInput, 1, wx.EXPAND | wx.ALL, 0)

        bSizer7.Add(sbSizer4, 10, wx.EXPAND, 5)

        sbSizer5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"输出文件output.txt"), wx.VERTICAL)

        self.richTextOutput = wx.richtext.RichTextCtrl(sbSizer5.GetStaticBox(), wx.ID_ANY, u"output",
                                                       wx.DefaultPosition, wx.DefaultSize,
                                                       0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.TE_MULTILINE)
        sbSizer5.Add(self.richTextOutput, 1, wx.EXPAND | wx.ALL, 0)

        bSizer7.Add(sbSizer5, 10, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        # Connect Events
        self.templateChoice.Bind(wx.EVT_CHOICE, self.changeTemplate)

        self.init()

    def __del__(self):
        pass

    def init(self):
        self.changeTemplate(None)

    def changeTemplate(self, event):
        template = TemplateConfig.getConfig().get(self.templateChoice.GetStringSelection())
        self.templateDesc.SetLabel(template.get("desc"))
        self.inputLeft.SetValue(template.get("left"))
        self.inputRight.SetValue(template.get("right"))
        self.inputSeparator.SetValue(template.get("separator"))
