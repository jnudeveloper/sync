#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hashlib
import hash_algorithm


# *递归扫描本地目录生成哈希数组链表,执行成功后返回一个哈希数组链表
def create_filehashlist_by_scan_directory(local_path):
    return 1


# *反序列化U盘上的.synchash文件得到哈希数组链表，并将所有的flag置0后返回该哈希数组链表
def init_filehashlist_by_deserialization(u_path):
    return 1


# *递归扫描本地同步目录，根据哈希数组链表计算得到数组diff，no_in_local, no_in_udisk
# *返回计算后的三个数组diff，no_in_local, no_in_udisk
def compute_sync_list(filehashlist, local_path):
    return 1


# *将哈希数组链表序列化后存储到U盘上,
def serialize_filehashlist(filehashlist,udisk_path):
    return 1


class FileHashList(object):
    def __init__(self):
        self.List = []
        for i in range(hash_algorithm.sync_hash_length):
            self.List.append(None)

    # 根据文件名把FileHashNode对象存入到哈希数组链表中的适当位置
    def insert(self, fname):
        filehash = FileHashNode(fname)
        offset = hash_algorithm.Hash_Offset(fname)
        if self.List[offset] == None:
            self.List[offset] = filehash
        else:
            head = self.List[offset]
            while head != None:
                head = head.Next
            head.set_next(filehash)

    # *根据文件名在哈希数组链表中寻找相应的节点，如果找到，返回该节点，如果没有返回None
    def find_by_hash(self, fname):
        return None

    # *遍历哈希数组链表，将所有的FileHashNode的flag置0,成功后返回True
    def set_zero_flag(self):
        return True

    # *遍历哈希数组链表，返回所有flag为0的FileHashNode是对应的文件名（即no_in_local数组）
    def get_no_in_local(self):
        return 1


class FileHashNode(object):
    def __init__(self, name):
        self.Name = name  # name为文件名字符串
        self.Next = None
        self.Flag = 0
        self.Name_Hashcode = hash_algorithm.Name_Hash(self.Name)
        self.Content_Hashcode = hash_algorithm.Content_Hash(self.Name)

    def set_next(self, fileHash):
        self.Next = fileHash

    def get_next(self):
        return self.Next

    def get_namehashcode(self):
        return self.Name_Hashcode

    def get_contenthashcode(self):
        return self.Content_Hashcode

    def get_fname(self):
        return self.Name

    def set_flag(self, flag):
        self.Flag = flag  # 初始化flag=0  0：本地无此文件 1：本地文件与U盘一致  2：本地文件与U盘不一致  3：U盘无此文件

    def get_flag(self):
        return self.Flag
