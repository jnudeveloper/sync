# coding=utf-8
import wx


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'Sync', pos=wx.DefaultPosition,
                          size=wx.Size(461, 356), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"重置", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem1)
        self.Bind(wx.EVT_MENU,self.ReSet,self.m_menuItem1)

        self.m_menuItem2 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"重启", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem2)
        self.Bind(wx.EVT_MENU,self.ReStart,self.m_menuItem2)

        self.m_menuItem3 = wx.MenuItem(self.m_menu1, wx.ID_ANY, u"帮助", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.Append(self.m_menuItem3)
        self.Bind(wx.EVT_MENU,self.Help,self.m_menuItem3)


        self.m_menubar1.Append(self.m_menu1, u"菜单")

        self.SetMenuBar(self.m_menubar1)


        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"本地：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        gSizer2.Add(self.m_staticText1, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        gSizer2.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"U盘：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        gSizer2.Add(self.m_staticText2, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.m_dirPicker2 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        gSizer2.Add(self.m_dirPicker2, 0, wx.ALL, 5)

        bSizer2.Add(gSizer2, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"选择"), wx.VERTICAL)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_button1 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"1.增量pull", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button1.Bind(wx.EVT_BUTTON, self.on_button1_click_event)

        self.m_button2 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"2.增量push", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button2.Bind(wx.EVT_BUTTON, self.on_button2_click_event)

        self.m_button3 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"3.全量pull", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button3, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button3.Bind(wx.EVT_BUTTON, self.on_button3_click_event)

        self.m_button4 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"4.全量push", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button4, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button4.Bind(wx.EVT_BUTTON, self.on_button4_click_event)

        self.m_button5 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"5.手动删除U盘上的全量目录", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        gSizer1.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button5.Bind(wx.EVT_BUTTON, self.on_button5_click_event)

        self.m_button6 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"6.初始化本地已有目录", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        gSizer1.Add(self.m_button6, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button6.Bind(wx.EVT_BUTTON, self.on_button6_click_event)

        self.m_button7 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"7.初始化U盘", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        gSizer1.Add(self.m_button7, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button7.Bind(wx.EVT_BUTTON, self.on_button7_click_event)

        self.m_button8 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"8.退出程序", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button8, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_button8.Bind(wx.EVT_BUTTON, self.on_button8_click_event)


        sbSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer1, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"欢迎使用Sync同步软件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def on_button1_click_event(self, event):
        event.Skip()

    def on_button2_click_event(self, event):
        event.Skip()

    def on_button3_click_event(self, event):
        event.Skip()

    def on_button4_click_event(self, event):
        event.Skip()

    def on_button5_click_event(self, event):
        event.Skip()

    def on_button6_click_event(self, event):
        event.Skip()

    def on_button7_click_event(self, event):
        event.Skip()

    def on_button8_click_event(self, event):
        event.Skip()

    def ReStart(self,event):
        event.Skip()

    def ReSet(self,event):
        event.Skip()

    def Help(self,event):
        event.Skip()