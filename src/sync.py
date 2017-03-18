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
# def init_udisk():
#     # TODO 初始化相关的操作，新建各个需要的目录等等（类似git)
#     f = open(path.udisk_path + os.sep + ".synchash", 'w')
#     f.close()
#     pass
#
#
# # 初始化本地的目录
# def init_local():
#     # TODO 初始化相关的操作，新建各个需要的目录等等（类似git)
#     f = open(path.local_path + os.sep + ".synchash", 'w')
#     f.close()
#     pass
# 上面两个函数不要了，直接用下面一个函数即可
def init_project(sync_path):
    f = open(sync_path + os.sep + ".synchash", 'w')
    f.close()


# 把U盘的数据传到本地
def udisk_to_local():
    # TODO
    # shutil.copytree(path.udisk_path, path.local_path + os.pathsep + "test")
    sync_copy_tree(path.udisk_path, path.local_path)  # + os.sep + "sync"
    print "成功把U盘的数据传到本地"


# 把本地的数据传到U盘
def local_to_udisk():
    # TODO 数据分块、重复数据消除、数据同步
    # shutil.copytree(path.local_path, path.udisk_path + os.sep + "sync")
    sync_copy_tree(path.local_path, path.udisk_path)  # + os.sep + "sync"
    print "成功把本地的数据传到U盘"


# TODO 流程1中的pull操作
def pull():
    return 1


# TODO 流程1中的push操作
def push():
    return 1


# TODO 移动文件到U盘,relative_path是相对同步根目录的路径
def move_to_udisk(relative_pathh):
    return 1


# TODO 移动文件到本地,relative_path是相对同步根目录的路径
def move_to_local(relative_pathh):
    return 1


# TODO 删除U盘中的文件,relative_path是相对同步根目录的路径
def delete_from_udisk(relative_pathh):
    return 1


# TODO 删除本地中的文件,relative_path是相对同步根目录的路径
def delete_from_local(relative_pathh):
    return 1


# TODO 递归扫描本地目录生成哈希数组链表,执行成功后返回一个哈希数组链表
def create_file_hash_list_by_scan_directory(path):
    return 1


# TODO 反序列化U盘上的.synchash文件得到哈希数组链表，并将所有的flag置0后返回该哈希数组链表
def init_file_hash_list_by_deserialization(path):
    return 1


# TODO 将哈希数组链表序列化
def serialize_file_hash_list(file_hash_list, path):
    return 1
