import wx
import wx.richtext as rt


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.rtc = rt.RichTextCtrl(panel, style=wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.TE_MULTILINE)
        vbox.Add(self.rtc, 1, flag=wx.EXPAND)

        panel.SetSizer(vbox)

        self.write_text_with_newline("Hello, this is a new line.\nThis is the second line.")

    def write_text_with_newline(self, text):
        attr = rt.RichTextAttr()
        self.rtc.BeginStyle(attr)
        self.rtc.WriteText(text)
        self.rtc.EndAllStyles()


app = wx.App(False)
frame = MyFrame(None, "RichTextCtrl 换行示例")
frame.Show()
app.MainLoop()
