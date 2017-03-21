#!/usr/bin/python
# coding=utf-8
# 测试path模块
from __future__ import absolute_import
import unittest
import os
from src import path


class TestPath(unittest.TestCase):
    # 测试方法：delete_last_slash
    def test_delete_last_slash(self):
        init_paths = ["d:\\dd\\", "d:\\dd\\\\", "d:\\dd", "E:/aa/", "E:/aa", "/usr/bin//", "/usr/bin/", "/usr/bin"]
        expect_paths = ["d:\\dd", "d:\\dd", "d:\\dd", "E:/aa", "E:/aa", "/usr/bin", "/usr/bin", "/usr/bin"]
        i = 0
        length = len(init_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.delete_last_slash(init_paths[i]))
            i += 1

    # 测试方法：add_last_slash
    def test_add_last_slash(self):
        init_paths = ["d:\\dd", "e:\\dd\\", "E:/aa", "/usr/bin", "/usr/bin/"]
        expect_paths = ["d:\\dd" + os.sep, "e:\\dd" + os.sep, "E:/aa" + os.sep, "/usr/bin" + os.sep,
                        "/usr/bin" + os.sep]
        i = 0
        length = len(init_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.add_last_slash(init_paths[i]))
            i += 1

    # 测试方法：change_local_absolute_path_to_relative_path
    def test_change_local_absolute_path_to_relative_path(self):
        path.local_path = "/usr/bin"
        absolute_paths = ["/usr/bin/path", "/usr/bin/path/", "/usr/bin/path/test", "/usr/bin/path/test/"]
        expect_paths = ["path", "path", "path/test", "path/test"]
        i = 0
        length = len(absolute_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.change_local_absolute_path_to_relative_path(absolute_paths[i]))
            i += 1

    # 测试方法：change_local_relative_path_to_absolute_path
    def test_change_local_relative_path_to_absolute_path(self):
        path.local_path = "/usr/bin"
        relative_paths = ["path", "path/", "/path", "/path/", "path/test", "path/test/"]
        expect_paths = ["/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path",
                        "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path/test",
                        "/usr/bin" + os.sep + "path/test"]
        i = 0
        length = len(relative_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.change_local_relative_path_to_absolute_path(relative_paths[i]))
            i += 1

    # 测试方法：change_udisk_absolute_path_to_relative_path
    def test_change_udisk_absolute_path_to_relative_path(self):
        path.udisk_path = "/usr/bin"
        absolute_paths = ["/usr/bin/path", "/usr/bin/path/", "/usr/bin/path/test", "/usr/bin/path/test/"]
        expect_paths = ["path", "path", "path/test", "path/test"]
        i = 0
        length = len(absolute_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.change_udisk_absolute_path_to_relative_path(absolute_paths[i]))
            i += 1

    # 测试方法：change_udisk_relative_path_to_absolute_path
    def test_change_udisk_relative_path_to_absolute_path(self):
        path.udisk_path = "/usr/bin"
        relative_paths = ["path", "path/", "/path", "/path/", "path/test", "path/test/"]
        expect_paths = ["/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path",
                        "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path/test",
                        "/usr/bin" + os.sep + "path/test"]
        i = 0
        length = len(relative_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.change_udisk_relative_path_to_absolute_path(relative_paths[i]))
            i += 1
