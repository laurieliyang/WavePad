import wx
import config

APP_MAIN = wx.App(False)
MKDN_PAD = None
HTML_PAD = None

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        MAIN_SIZER = wx.BoxSizer(wx.HORIZONTAL)
        MKDN_PAD = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        HTML_PAD = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        MAIN_SIZER.Add(MKDN_PAD, wx.EXPAND|wx.TOP)
        MAIN_SIZER.Add(HTML_PAD, wx.EXPAND|wx.TOP)
        
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        

mainFrm = MainFrame(parent=None, title='WavePad - ' + config.getVersion())
mainFrm.Show()

APP_MAIN.MainLoop()

