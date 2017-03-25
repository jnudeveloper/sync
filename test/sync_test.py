#!/usr/bin/python
# coding=utf-8
# 测试sync模块
import os
from src import sync
from src import synchash
import shutil
from shutil import copytree
from src import serialize
from src import path


# 测试方法：move_one_file(src, sync_path, relative_path)
def test_move_one_file():
    src = 'E:\\test\\local\\A\\B\\C\\a.txt'
    sync_path = 'E:\\test\\udisk'
    relative_path = 'A\\B\\C\\a.txt'
    sync.move_one_file(src, sync_path, relative_path)


# test_move_one_file()


# 测试遍历目录下的文件
def traverse_sync(path):
    file_path_arr = []
    for root, dirs, files in os.walk(path):
        for files_path in files:
            file_path_arr.append(os.path.join(root, files_path))
    return file_path_arr


# 获取同步目录下除.sync目录下的所有文件路径
def get_all_file_path(sync_path):
    file_path_arr = []
    folders = os.listdir(sync_path)
    for folder in folders:
        if folder == ".sync":
            pass
        elif os.path.isfile(sync_path + os.sep + folder):
            file_path_arr.append(sync_path + os.sep + folder)
        elif os.path.isdir(sync_path + os.sep + folder):
            file_path_arr.extend(traverse_sync(sync_path + os.sep + folder))
    return file_path_arr


# 测试
# path = "E:\\py_test\\test"
# print(traverse_sync(path))
# print(get_all_file_path(path))

# 测试sync.py中的四个文件操作函数
# local_path = "E:\\py_test\\test"
# udisk_path = "E:\\py_test\\other"
# relative_path = "A\\a.txt"
# node = synchash.FileHashNode(local_path, relative_path)
# sync.move_to_udisk(local_path, udisk_path, node)
# sync.move_to_local(udisk_path, local_path, node)
# sync.delete_from_udisk(udisk_path, node)
# sync.delete_from_local(local_path, node)


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


# udisk_path = "E:\\py_test\\other"
# local_path = "E:\\py_test\\test"

# fully_pull(udisk_path, local_path)

# shutil.rmtree(udisk_path + os.sep + ".sync" + os.sep + ".all")


# TODO 由于synchash.fill_sync_hash_list(sync_hash_list)还未实现，所以这个函数没有测试 shiweihua
# 本地项目初始化  见本地项目初始化流程图 shiweihua
def init_local():
    # 新建一个sync_hash数组链表 shiweihua
    sync_hash_list = synchash.FileHashList()
    # 递归扫描本地同步目录填充sync_hash数组链表 shiweihua
    sync_hash_list = synchash.fill_sync_hash_list(sync_hash_list)
    # 将sync_hash_list序列化到本地
    serialize.serialize(sync_hash_list, path.local_path + os.sep + ".sync")


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


udisk_path = "E:\\py_test\\other"
local_path = "E:\\py_test\\test"

fully_push(local_path, udisk_path)
