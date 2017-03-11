# coding=utf-8
# 同步相关的代码
import os
import path
import shutil


# 同步整个目录树，即使目标文件夹已经存在
def sync_copy_tree(src, dst):
    names = os.listdir(src)
    for name in names:
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        if os.path.isdir(src_name):
            if not os.path.exists(dst_name):
                # 目录不存在时，创建目录
                os.mkdir(dst_name)
            sync_copy_tree(src_name, dst_name)
        elif name != ".synchash":
            # 不同步文件 .synchash
            shutil.copy2(src_name, dst_name)


# 初始化U盘的目录
def init_usb():
    # TODO 初始化相关的操作，新建各个需要的目录等等（类似git)
    f = open(path.usb_path + os.sep + ".synchash", 'w')
    f.close()
    pass


# 初始化本地的目录
def init_local():
    # TODO 初始化相关的操作，新建各个需要的目录等等（类似git)
    f = open(path.local_path + os.sep + ".synchash", 'w')
    f.close()
    pass


# 把U盘的数据传到本地
def usb_to_local():
    # TODO
    # shutil.copytree(path.usb_path, path.local_path + os.pathsep + "test")
    sync_copy_tree(path.usb_path, path.local_path)  # + os.sep + "sync"
    print "成功把U盘的数据传到本地"


# 把本地的数据传到U盘
def local_to_usb():
    # TODO 数据分块、重复数据消除、数据同步
    # shutil.copytree(path.local_path, path.usb_path + os.sep + "sync")
    sync_copy_tree(path.local_path, path.usb_path)  # + os.sep + "sync"
    print "成功把本地的数据传到U盘"
