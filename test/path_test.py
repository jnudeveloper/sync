#!/usr/bin/python
# coding=utf-8
# 测试path模块
from __future__ import absolute_import
import unittest
from src import path


class TestPath(unittest.TestCase):
    # 测试方法：delete_last_slash
    def test_delete_last_slash(self):
        init_paths = ["d:\\dd\\", "d:\\dd\\\\", "d:\\dd\\", "E:/aa/", "E:/aa", "/usr/bin//", "/usr/bin/", "/usr/bin"]
        expect_paths = ["d:\\dd", "d:\\dd",  "d:\\dd", "E:/aa", "E:/aa", "/usr/bin", "/usr/bin", "/usr/bin"]
        i = 0
        length = len(init_paths)
        while i < length:
            self.assertEqual(expect_paths[i], path.delete_last_slash(init_paths[i]))
            i += 1
