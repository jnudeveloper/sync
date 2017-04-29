# coding=utf-8
# 流程的具体细节（图形界面）
import gui
import wx
import prompt
import path
import hash_algorithm
import serialize
import os
import sync
import shutil
import synchash
import path_win


# 脚本运行

class MyFrame(gui.MyFrame1):
    def __init__(self, parent, title):
        gui.MyFrame1.__init__(self, parent)
        self.number_of_clicks = 0

    def on_button1_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        path.udisk_path = self.m_dirPicker2.GetPath()
        local_path_test = path_win.is_path_valid_and_is_project_exists(path.local_path)
        udisk_path_test = path_win.is_path_valid_and_is_project_exists_and_is_dir_same(path.udisk_path)
        self.m_staticText3.SetLabelText("")
        if local_path_test and udisk_path_test:
            sync.incrementally_pull()
            self.m_staticText3.SetLabelText("执行增量pull完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button2_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        path.udisk_path = self.m_dirPicker2.GetPath()
        local_path_test = path_win.is_path_valid_and_is_project_exists(path.local_path)
        udisk_path_test = path_win.is_path_valid_and_is_project_exists_and_is_dir_same(path.udisk_path)
        self.m_staticText3.SetLabelText("")
        if local_path_test and udisk_path_test:
            sync.incrementally_push()
            self.m_staticText3.SetLabelText("执行增量push完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button3_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        path.udisk_path = self.m_dirPicker2.GetPath()
        local_path_test = path_win.is_path_valid_and_is_path_empty(path.local_path)
        udisk_path_test = path_win.is_path_valid_and_is_project_exists_and_is_dir_sameand_has_all_the_project(
            path.udisk_path)
        self.m_staticText3.SetLabelText("")
        if local_path_test and udisk_path_test:
            sync.fully_pull(path.udisk_path, path.local_path)
            self.m_staticText3.SetLabelText("执行全量pull完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button4_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        path.udisk_path = self.m_dirPicker2.GetPath()
        local_path_test = path_win.is_path_valid_and_is_project_exists(path.local_path)
        udisk_path_test = path_win.is_path_valid_and_is_project_exists_and_is_dir_same(path.udisk_path)
        self.m_staticText3.SetLabelText("")
        if local_path_test and udisk_path_test:
            sync.init_local()
            sync.fully_push(path.local_path, path.udisk_path)
            self.m_staticText3.SetLabelText("执行全量push完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button5_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        path.udisk_path = self.m_dirPicker2.GetPath()
        # 检查U盘上是否已经有全量目录 shiweihua
        udisk_path_test = path_win.is_path_valid_and_is_project_exists(path.udisk_path)
        if not udisk_path_test:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")
        else:
            if os.path.exists(path.udisk_path + os.sep + ".sync" + os.sep + ".all"):
                # 如果有则删除U盘上的全量目录 shiweihua
                shutil.rmtree(path.udisk_path + os.sep + ".sync" + os.sep + ".all")
                self.m_staticText3.SetLabelText("删除全量目录成功，程序正常退出！")
            else:
                # 如果没有就提示没有全量目录，然后不做任何操作 shiweihua
                self.m_staticText3.SetLabelText("U盘上没有全量目录！程序正常退出！")

    def on_button6_click_event(self, event):
        path.local_path = self.m_dirPicker1.GetPath()
        # 本地项目初始化  见本地项目初始化流程图 shiweihua
        local_path_test = path_win.is_path_valid_and_is_project_not_exists(path.local_path)
        self.m_staticText3.SetLabelText("")
        if local_path_test:
            sync.init_local()
            self.m_staticText3.SetLabelText("本地项目初始化完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button7_click_event(self, event):
        path.udisk_path = self.m_dirPicker2.GetPath()
        # 初始化U盘
        udisk_path_test = path_win.is_path_valid_and_is_path_empty(path.udisk_path)
        self.m_staticText3.SetLabelText("")
        if udisk_path_test:
            sync.init_udisk()
            self.m_staticText3.SetLabelText("U盘初始化完成，程序正常退出！")
        else:
            self.m_staticText3.SetLabelText("路径选择错误，请重新选择")

    def on_button8_click_event(self, event):
        self.Close()



class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, "Hello sync")
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True


def run():
    app = MyApp()
    app.MainLoop()
