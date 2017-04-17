# coding=utf-8
# 流程的具体细节（图形界面）
import Tkinter
import tkFileDialog


# 脚本运行
def run():
    root = Tkinter.Tk()
    width = 400  # 窗口宽度
    height = 300  # 窗口高度
    root.geometry("%sx%s+%s+%s" % (
        width,  # 窗口宽度
        height,  # 窗口高度
        (root.winfo_screenwidth() - width) / 2,  # 窗口水平居中
        (root.winfo_screenheight() - height) / 2  # 窗口垂直居中
    ))
    root.title("同步工具")
    root.resizable(width=False, height=False)  # 窗口宽度和高度不可以改变
    #  定义变量
    entry_local = Tkinter.StringVar()
    entry_udisk = Tkinter.StringVar()

    # tkFileDialog.askdirectory()
    frm_top = Tkinter.Frame(root, height=20)
    Tkinter.Label(frm_top, text="本地目录", font=('Arial', 15)).pack(side=Tkinter.LEFT)  # , width=10, height=5)
    Tkinter.Label(frm_top, text="U盘目录", font=('Arial', 15)).pack(side=Tkinter.RIGHT)  # , width=10, height=5)
    frm_top.pack(side=Tkinter.TOP)
    root.mainloop()

