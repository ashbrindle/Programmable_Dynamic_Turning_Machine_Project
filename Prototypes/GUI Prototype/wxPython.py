
import wx

def func():
    print "Hi"


vbox = wx.BoxSizer(wx.VERTICAL)
panel = wx.Panel()

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
frame.Show(True)

btn = wx.Button(panel,-1,"click Me")
vbox.Add(btn,0,wx.ALIGN_CENTER)
btn.Bind(wx.EVT_BUTTON,func)

app.MainLoop()