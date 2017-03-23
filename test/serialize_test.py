# coding=utf-8
# 测试selialize模块

from __future__ import absolute_import
import unittest
from src import serialize, synchash


class TestSerialize(unittest.TestCase):
    # 测试serialize、deserialize方法
    # author 李国雄
    def test_serialize_deserialize(self):
        hash_list = synchash.FileHashList()
        hash_node = synchash.FileHashNode("./__init__.py")
        hash_list.insert(hash_node)
        serialize.serialize(hash_list, ".")
        hash_list_new = serialize.deserialize(".")
        hash_node_new = hash_list_new.find_by_name_hashcode(hash_node.get_name_hashcode())
        print(hash_node.get_path())
        print(hash_node_new.get_path())
        self.assertEqual(hash_node.get_path(), hash_node_new.get_path())
        self.assertEqual(hash_node.get_name_hashcode(), hash_node_new.get_name_hashcode())
        self.assertEqual(hash_node.get_content_hashcode(), hash_node_new.get_content_hashcode())
        self.assertEqual(hash_node.get_next_node(), hash_node_new.get_next_node())
