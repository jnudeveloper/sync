#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hash_algorithm


class FileHashList(object):
    # TODO 测试node != None，是否可以这样写
    # TODO 是否可以显式定义属性

    def __init__(self):
        self.hash_list = []
        for i in range(hash_algorithm.sync_hash_length):
            self.hash_list.append(None)

    # 根据文件名把FileHashNode对象存入到哈希数组链表中的适当位置
    def insert(self, node):
        offset = hash_algorithm.get_hash_offset(node.get_name_hashcode())
        if self.hash_list[offset] == None:
            self.hash_list[offset] = node
        else:
            node.set_next_node(self.hash_list[offset])
            self.hash_list[offset] = node
            # temp_node = self.hash_list[offset]
            # while temp_node != None:
            #     temp_node = temp_node.get_next_node()
            # temp_node.set_next(node)

    # 根据文件名hash在哈希数组链表中寻找相应的节点，如果找到，返回该节点，如果没有返回None
    def find_by_name_hashcode(self, name_hashcode):
        offset = hash_algorithm.get_hash_offset(name_hashcode)
        node = self.hash_list[offset]
        while node != None:
            if name_hashcode == node.get_name_hashcode():
                return node
            else:
                node = node.get_next_node()
        return None

    # 遍历哈希数组链表，将所有的FileHashNode的flag置0,成功后返回True
    def reset_flag(self):
        for i in range(hash_algorithm.sync_hash_length):
            node = self.hash_list[i]
            while node != None:
                node.set_flag(0)
                node = node.get_next_node()
        return True

    # 遍历哈希数组链表，返回所有flag为0的FileHashNode相对应的文件名（即delete_in_local数组）
    def get_no_in_local(self):
        delete_in_local = []
        for i in range(hash_algorithm.sync_hash_length):
            node = self.hash_list[i]
            while node != None:
                if node.get_flag() == 0:
                    delete_in_local.append(node)
                node = node.get_next_node()
        return delete_in_local

    # 根据文件名hash删除节点
    # 出现异常返回 -1
    # 没有节点返回 -2
    def delete_by_name_hashcode(self, name_hashcode):
        # TODO 根据相对路径删除节点
        pass

    # 根据name_hashcode修改content_hashcode
    def change_content_hashcode_by_name_hashcode(self, name_hashcode):
        # TODO 根据name_hashcode修改content_hashcode
        pass

    # 根据name_hashcode修改flag
    def change_flag_by_name_hashcode(self, name_hashcode):
        # TODO 根据name_hashcode修改flag
        pass


class FileHashNode(object):
    def __init__(self, path):
        self.path = path  # path为相对路径
        self.nextNode = None  # 下一节点
        self.flag = 0  # 标志位，用于同步. 0: 在本地该文件已被删除；1：在本地该文件未被删除
        self.name_hashcode = hash_algorithm.get_name_hashcode(self.path)  # 文件名hash值
        self.content_hashcode = hash_algorithm.get_content_hashcode(self.path)  # 文件内容hash值

    def set_next_node(self, node):
        self.nextNode = node

    def get_next_node(self):
        return self.nextNode

    def get_name_hashcode(self):
        return self.name_hashcode

    def set_name_hashcode(self, path):
        self.name_hashcode = hash_algorithm.get_name_hashcode(path)

    def get_content_hashcode(self):
        return self.content_hashcode

    def set_content_hashcode(self, path):
        self.content_hashcode = hash_algorithm.get_content_hashcode(path)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def set_flag(self, flag):
        self.flag = flag

    def get_flag(self):
        return self.flag
