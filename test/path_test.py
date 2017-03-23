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

    # 测试方法：change_absolute_path_to_relative_path
    def test_change_absolute_path_to_relative_path(self):
        path.local_path = "/usr/bin"
        absolute_paths = ["/usr/bin/path", "/usr/bin/path/", "/usr/bin/path/test", "/usr/bin/path/test/"]
        expect_paths = ["path", "path", "path/test", "path/test"]
        i = 0
        length = len(absolute_paths)
        while i < length:
            self.assertEqual(expect_paths[i],
                             path.change_absolute_path_to_relative_path(path.local_path, absolute_paths[i]))
            i += 1

    # 测试方法：change_relative_path_to_absolute_path
    def test_change_relative_path_to_absolute_path(self):
        path.local_path = "/usr/bin"
        relative_paths = ["path", "path/", "/path", "/path/", "path/test", "path/test/"]
        expect_paths = ["/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path",
                        "/usr/bin" + os.sep + "path", "/usr/bin" + os.sep + "path/test",
                        "/usr/bin" + os.sep + "path/test"]
        i = 0
        length = len(relative_paths)
        while i < length:
            self.assertEqual(expect_paths[i],
                             path.change_relative_path_to_absolute_path(path.local_path, relative_paths[i]))
            i += 1

    # 测试方法：is_current_dir_same
    def test_is_current_dir_same(self):
        path.local_path = "/usr/local/test/"
        input_paths = ["/usr/disk" + os.sep + "test", "/usr/disk" + os.sep + "test/", "/usr/disk" + os.sep + "tests"]
        expect_output = [True, True, False]
        i = 0
        length = len(input_paths)
        while i < length:
            self.assertEqual(expect_output[i], path.is_current_dir_same(input_paths[i]))
            i += 1

    # 测试方法：is_project_exists
    def test_is_project_exists(self):
        if os.path.exists(".sync"):
            for item in os.listdir(".sync"):
                os.remove(".sync" + os.path.sep + item)
            os.removedirs(".sync")
        self.assertEqual(False, path.is_project_exists("."))
        os.mkdir(".sync")
        self.assertEqual(False, path.is_project_exists("."))
        file_new = file("." + os.path.sep + ".sync" + os.path.sep + ".synchash", "w")
        file_new.close()
        self.assertEqual(True, path.is_project_exists("."))

    # 测试方法：is_path_empty
    def test_is_path_empty(self):
        if os.path.exists(".sync"):
            for item in os.listdir(".sync"):
                os.remove(".sync" + os.path.sep + item)
            os.removedirs(".sync")
        os.mkdir(".sync")
        self.assertEqual(True, path.is_path_empty(".sync"))
        file_new = file("." + os.path.sep + ".sync" + os.path.sep + ".synchash", "w")
        file_new.close()
        self.assertEqual(False, path.is_path_empty(".sync"))
