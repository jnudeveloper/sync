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

test_move_one_file()

