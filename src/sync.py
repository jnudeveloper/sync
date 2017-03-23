# coding=utf-8
# 同步相关的代码
import os
import path
import shutil


# TODO 复制整个目录树U盘的.sync文件夹中 liguoxiong
# TODO 不用复制本地.sync文件夹 liguoxiong
# TODO 要复制到U盘的.sync文件夹中 liguoxiong
def sync_copy_tree_to_udisk(src, dst):
    names = os.listdir(src)
    for name in names:
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        if os.path.isdir(src_name):
            if not os.path.exists(dst_name):
                # 目录不存在时，创建目录
                os.mkdir(dst_name)
            sync_copy_tree_to_udisk(src_name, dst_name)
        elif name != ".synchash":
            # 不同步文件 .synchash
            shutil.copy2(src_name, dst_name)


# TODO 同步U盘的.sync文件夹整个目录树到本地 liguoxiong
def sync_copy_tree_to_local(src, dst):
    pass


# 初始化目录,新建.synchash文件
def init_project(sync_path):
    f = open(sync_path + os.sep + ".synchash", 'w')
    f.close()


# 把U盘的数据传到本地
def udisk_to_local():
    # TODO liguoxiong 没用的函数，先不写
    # shutil.copytree(path.udisk_path, path.local_path + os.pathsep + "test")
    sync_copy_tree(path.udisk_path, path.local_path)  # + os.sep + "sync"
    print "成功把U盘的数据传到本地"


# 把本地的数据传到U盘
def local_to_udisk():
    # TODO 数据分块、重复数据消除、数据同步   liguoxiong 没用的函数，先不写
    # shutil.copytree(path.local_path, path.udisk_path + os.sep + "sync")
    sync_copy_tree(path.local_path, path.udisk_path)  # + os.sep + "sync"
    print "成功把本地的数据传到U盘"


# @author shiweihua
# 根据节点信息，把本地文件移动到U盘（如果文件已经存在，则覆盖） shiweihua
def move_to_udisk(local_path, udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（local_absolute_path）
    local_absolute_path = path.change_relative_path_to_absolute_path(local_path, relative_path)
    # 把本地文件移动到U盘
    move_one_file(local_absolute_path, udisk_path, relative_path)


# @author shiweihua
# 根据节点信息，把U盘文件移动到本地(如果文件已经存在，则覆盖) shiweihua
def move_to_local(local_path, udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（udisk_absolute_path）
    udisk_absolute_path = path.change_relative_path_to_absolute_path(udisk_path, relative_path)
    # 把本地文件移动到本地
    move_one_file(udisk_absolute_path, local_path, relative_path)


# @author shiweihua
# 根据节点信息,删除U盘中的文件 shiweihua
def delete_from_udisk(udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（udisk_absolute_path）
    udisk_absolute_path = path.change_relative_path_to_absolute_path(udisk_path, relative_path)
    # 如果存在这个文件，则删掉它
    if os.path.exists(udisk_absolute_path):
        os.remove(udisk_absolute_path)


# @author shiweihua
# 根据节点信息,删除本地中的文件 shiweihua
def delete_from_local(local_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（local_absolute_path）
    local_absolute_path = path.change_relative_path_to_absolute_path(local_path, relative_path)
    # 如果存在这个文件，则删掉它
    if os.path.exists(local_absolute_path):
        os.remove(local_absolute_path)


# @author shiweihua
# 根据给出的路径移动文件，需要时会自动新建目录 shiweihua
def move_one_file(src, sync_path, relative_path):
    # 将relative_path按路径分隔符切割成数组relative_path_arr
    relative_path_arr = relative_path.split(os.sep)
    # 删除relative_path_arr中最后一个元素
    relative_path_arr.pop()
    # 逐步将sync_path与relative_path_arr中的元素拼接，并且检验这个目录是否存在，不存在则新建之
    tmp_sync_path = sync_path
    for tmp_folder in relative_path_arr:
        tmp_sync_path += (os.sep + tmp_folder)
        if not os.path.exists(tmp_sync_path):
            os.mkdir(tmp_sync_path)  # 目录不存在，新建之
    # 如果目的文件夹下已经存在这个文件则覆盖它，否则复制文件到目的文件夹下
    shutil.copy2(src, sync_path + os.sep + relative_path)
