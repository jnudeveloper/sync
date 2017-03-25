# coding=utf-8
# 同步相关的代码
import os
import path
import shutil
from shutil import copytree
import synchash
import serialize


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
# TODO 和delete_from_udisk差不多，可不可以合成一个？ shiweihua
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


# @author shiweihua
# 把U盘中的全量目录pull到本地
def fully_pull(udisk_path, local_path):
    full_dir = udisk_path + os.sep + ".sync" + os.sep + ".all"
    folders = os.listdir(full_dir)
    for folder in folders:
        full_src_path = full_dir + os.sep + folder
        if os.path.isdir(full_src_path):
            copytree(full_src_path, local_path + os.sep + folder)
        elif os.path.isfile(full_src_path):
            shutil.copy2(full_src_path, local_path)
    # 在本地新建.sync目录
    os.mkdir(local_path + os.sep + ".sync")
    shutil.copy2(udisk_path + os.sep + ".sync" + os.sep + ".synchash",
                 local_path + os.sep + ".sync" + os.sep + ".synchash")


# @author shiweihua
# 将本地的所有文件复制到U盘的全量目录下
def fully_push(local_path, udisk_path):
    if os.path.exists(udisk_path + os.sep + ".sync" + os.sep + ".all"):
        shutil.rmtree(udisk_path + os.sep + ".sync" + os.sep + ".all")
    full_dst_dir = udisk_path + os.sep + ".sync" + os.sep + ".all"
    os.mkdir(full_dst_dir)
    folders = os.listdir(local_path)
    for folder in folders:
        if folder != ".sync":
            full_src_path = local_path + os.sep + folder
            if os.path.isdir(full_src_path):
                copytree(full_src_path, full_dst_dir + os.sep + folder)
            elif os.path.isfile(full_src_path):
                shutil.copy2(full_src_path, full_dst_dir)


# TODO 由于synchash.fill_sync_hash_list(sync_hash_list)还未实现，所以这个函数没有测试 shiweihua
# 本地项目初始化  见本地项目初始化流程图 shiweihua
def init_local():
    # 新建一个sync_hash数组链表 shiweihua
    sync_hash_list = synchash.FileHashList()
    # 递归扫描本地同步目录填充sync_hash数组链表 shiweihua
    sync_hash_list = synchash.fill_sync_hash_list(sync_hash_list)
    # 将sync_hash_list序列化到本地
    serialize.serialize(sync_hash_list, path.local_path + os.sep + ".sync")


# TODO 未测试 shiweihua
# 初始化U盘
def init_udisk():
    # 在U盘上新建.sync文件夹， 在文件夹.sync中新建.synchash空文件 shiweihua
    os.mkdir(path.udisk_path + os.sep + ".sync")
    os.mknod(path.udisk_path + os.sep + ".sync" + os.sep + ".synchash")
    # 初始化一个sync_hash空数组链表，序列化到U盘的.sync文件夹下的.synchash文件中 shiweihua
    sync_hash = synchash.FileHashList()
    serialize.serialize(sync_hash, path.udisk_path + os.sep + ".sync")
