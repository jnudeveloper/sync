#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hashlib
import hash_algorithm


class FileHashList(object):
    def __init__(self):
        self.List = []
        for i in range(hash_algorithm.sync_hash_length):
            self.List.append(None)

    def insert(self, fname):
        filehash = FileHashNode(fname)
        offset = filehash.get_namehashcode()
        if self.List[offset] == None:
            self.List[offset] = filehash
        else:
            head = self.List[offset]
            while head != None:
                head = head.Next
            head.set_next(filehash)


class FileHashNode(object):
    def __init__(self, name):
        self.Name = name  # name为文件名字符串
        self.Next = None
        self.Flag = 0
        self.Name_Hashcode = 0
        self.Content_Hashcode = 0

    def set_next(self, fileHash):
        self.Next = fileHash

    def get_next(self):
        return self.Next

    def get_namehashcode(self):
        self.Name_Hashcode = hash_algorithm.Name_Hash(self.Name)
        return self.Name_Hashcode

    def get_contenthashcode(self):
        self.Content_Hashcode = hash_algorithm.Content_Hash(self.Name)
        return self.Content_Hashcode

    def get_fname(self):
        return self.Name

    def set_flag(self, flag):
        self.Flag = flag;  # 初始化flag=0  0：本地无此文件 1：本地文件与U盘一致  2：本地文件与U盘不一致  3：U盘无此文件

    def get_flag(self):
        return self.Flag
