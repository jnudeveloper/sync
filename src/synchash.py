#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hash_algorithm


class FileHashList(object):
    def __init__(self):
        self.list = []
        for i in range(hash_algorithm.sync_hash_length):
            self.list.append(None)

    # 根据文件名把FileHashNode对象存入到哈希数组链表中的适当位置
    def insert(self, filename):
        file_hash = FileHashNode(filename)
        offset = hash_algorithm.get_hash_offset(filename)
        if self.list[offset] == None:
            self.list[offset] = file_hash
        else:
            head = self.list[offset]
            while head != None:
                head = head.Next
            head.set_next(file_hash)

    # 根据文件名在哈希数组链表中寻找相应的节点，如果找到，返回该节点，如果没有返回None
    def find_by_filename(self, fname):
        offset = hash_algorithm.get_hash_offset(fname)
        node = self.list[offset]
        name_hash = hash_algorithm.get_name_hash(fname)
        while node != None:
            if name_hash == node.get_namehashcode():
                return node
            else:
                node = node.Next
        return None

    # 遍历哈希数组链表，将所有的FileHashNode的flag置0,成功后返回True
    def set_zero_flag(self):
        for i in range(hash_algorithm.sync_hash_length):
            node = self.list[i]
            while node != None:
                node.Flag = 0
                node = node.Next
        return True

    # 遍历哈希数组链表，返回所有flag为0的FileHashNode相对应的文件名（即no_in_local数组）
    def get_no_in_local(self):
        no_in_local = []
        for i in range(hash_algorithm.sync_hash_length):
            node = self.list[i]
            while node != None:
                if node.Flag == 0:
                    no_in_local.append(node.get_fname)
                node = node.Next
        return no_in_local


class FileHashNode(object):
    def __init__(self, name):
        self.name = name  # name为文件名字符串
        self.next = None
        self.flag = 0
        self.name_hashcode = hash_algorithm.get_name_hash(self.name)
        self.content_hashcode = hash_algorithm.get_content_hash(self.name)

    def set_next(self, file_hash):
        self.next = file_hash

    def get_next(self):
        return self.next

    def get_name_hashcode(self):
        return self.name_hashcode

    def get_content_hashcode(self):
        return self.content_hashcode

    def get_file_name(self):
        return self.name

    def set_flag(self, flag):
        self.flag = flag  # 初始化flag=0  0：本地无此文件 1：本地文件与U盘一致  2：本地文件与U盘不一致  3：U盘无此文件

    def get_flag(self):
        return self.flag
