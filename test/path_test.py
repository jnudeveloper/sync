#!/usr/bin/python
# coding=utf-8
# 测试path模块
from __future__ import absolute_import
import unittest
import os
from src import path


class TestPath(unittest.TestCase):
    # 测试方法：delete_last_slash
    # author 李国雄
    def test_delete_last_slash(self):
        init_paths = ["d:\\dd\\", "d:\\dd\\\\", "d:\\dd", "E:/aa/", "E:/aa", "/usr/bin//", "/usr/bin/", "/usr/bin"]
        expect_paths = ["d:\\dd", "d:\\dd", "d:\\dd", "E:/aa", "E:/aa", "/usr/bin", "/usr/bin", "/usr/bin"]
        i = 0
        length = len(init_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.delete_last_slash(init_paths[i]))
            i += 1

    # 测试方法：add_last_slash
    # author 李国雄
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
    # author 李国雄
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
    # author 李国雄
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
    # author 李国雄
    def test_is_current_dir_same(self):
        path.local_path = "/usr/local/test/"
        input_paths = ["/usr/disk" + os.sep + "test", "/usr/disk" + os.sep + "test/", "/usr/disk" + os.sep + "tests"]
        expect_output = [True, True, False]
        i = 0
        length = len(input_paths)
        while i < length:
            self.assertEqual(expect_output[i], path.is_current_dir_same(input_paths[i], path.local_path))
            i += 1

    # 测试方法：is_project_exists
    # author 李国雄
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
    # author 李国雄
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

    # 测试方法：is_path_valid
    # author 李国雄
    def test_is_path_valid(self):
        self.assertEqual(True, path.is_path_valid("."))
        self.assertEqual(False, path.is_path_valid("." + os.path.sep + ".sync"))
        self.assertEqual(True, path.is_path_valid(".." + os.path.sep + "src"))

    # 测试方法：is_path_valid_and_is_project_exists
    # author 李国雄
    def test_is_path_valid_and_is_project_exists(self):
        if os.path.exists(".sync"):
            for item in os.listdir(".sync"):
                os.remove(".sync" + os.path.sep + item)
            os.removedirs(".sync")
        self.assertEqual(False, path.is_path_valid_and_is_project_exists("."))
        os.mkdir(".sync")
        self.assertEqual(False, path.is_path_valid_and_is_project_exists("."))
        file_new = file("." + os.path.sep + ".sync" + os.path.sep + ".synchash", "w")
        file_new.close()
        self.assertEqual(True, path.is_path_valid_and_is_project_exists("."))

    # 测试方法：is_path_valid_and_is_project_not_exists
    # author 李国雄
    def test_is_path_valid_and_is_project_not_exists(self):
        if os.path.exists(".sync"):
            for item in os.listdir(".sync"):
                os.remove(".sync" + os.path.sep + item)
            os.removedirs(".sync")
        self.assertEqual(True, path.is_path_valid_and_is_project_not_exists("."))
        os.mkdir(".sync")
        self.assertEqual(True, path.is_path_valid_and_is_project_not_exists("."))
        file_new = file("." + os.path.sep + ".sync" + os.path.sep + ".synchash", "w")
        file_new.close()
        self.assertEqual(False, path.is_path_valid_and_is_project_not_exists("."))

    # 测试方法：is_path_valid_and_is_project_exists_and_is_dir_same
    # author 李国雄
    def test_is_path_valid_and_is_project_exists_and_is_dir_same(self):
        if os.path.exists(".sync"):
            for item in os.listdir(".sync"):
                os.remove(".sync" + os.path.sep + item)
            os.removedirs(".sync")
        path.local_path = "/usr" + os.sep + "test"
        self.assertEqual(False, path.is_path_valid_and_is_project_exists_and_is_dir_same(".." + os.path.sep + "test"))
        os.mkdir(".sync")
        self.assertEqual(False, path.is_path_valid_and_is_project_exists_and_is_dir_same(".." + os.path.sep + "test"))
        file_new = file("." + os.path.sep + ".sync" + os.path.sep + ".synchash", "w")
        file_new.close()
        self.assertEqual(True, path.is_path_valid_and_is_project_exists_and_is_dir_same(".." + os.path.sep + "test"))

    # 测试方法：is_path_valid_and_is_path_empty
    # author 李国雄
    def test_is_path_valid_and_is_path_empty(self):
        if os.path.exists("." + os.path.sep + "test"):
            for item in os.listdir("." + os.path.sep + "test"):
                os.remove("." + os.path.sep + "test" + os.path.sep + item)
            os.removedirs("." + os.path.sep + "test")
        self.assertEqual(False, path.is_path_valid_and_is_path_empty("." + os.path.sep + "test"))
        os.mkdir("test")
        self.assertEqual(True, path.is_path_valid_and_is_path_empty("." + os.path.sep + "test"))
        file_new = file("." + os.path.sep + "test" + os.path.sep + "a.txt", "w")
        file_new.close()
        self.assertEqual(False, path.is_path_valid_and_is_path_empty("." + os.path.sep + "test"))
