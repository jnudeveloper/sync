#!/usr/bin/python
# coding=utf-8
# 测试sync模块
import os
from src import sync


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
path = "E:\\py_test\\test"
print(traverse_sync(path))
print(get_all_file_path(path))











