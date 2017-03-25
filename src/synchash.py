#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hash_algorithm
import path


class FileHashList(object):
    #  测试node != None，是否可以这样写 skywhat
    #  写成 node is not None
    #  是否可以显式定义属性 skywhat
    #  初始化定义属性，分清类属性与实例属性的区别

    def __init__(self):
        self.hash_list = [None] * hash_algorithm.sync_hash_length

    # 根据文件名把FileHashNode对象存入到哈希数组链表中的适当位置
    def insert(self, node):
        offset = hash_algorithm.get_hash_offset(node.get_name_hashcode())
        if self.hash_list[offset] is None:
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
        while node is not None:
            if name_hashcode == node.get_name_hashcode():
                return node
            else:
                node = node.get_next_node()
        return None

    # 根据文件名hash删除节点
    # 出现异常返回 -1
    # 找不到name_hashcode对应的节点返回 -2
    #  如果被删掉的node是FileHashList某条链表中剩下的最后一个节点了，则要把这个数组元素置为None，如果不理解这段话找shiweihua
    def delete_by_name_hashcode(self, name_hashcode):
        #  根据相对路径删除节点  skywhat
        offset=hash_algorithm.get_hash_offset(name_hashcode)
        node=self.hash_list[offset]
        while node is not None and node.name_hashcode != name_hashcode:
            node=node.next_node
        if node is None:
            return -1
        if node.next_node is None:
            node=None
        else:
            node.path=node.next_node.path
            node.name_hashcode=node.next_node.name_hashcode
            node.content_hashcode=node.next_node.content_hashcode
            node.next_node=node.next_node.next_node

    # 根据name_hashcode修改content_hashcode
    def change_content_hashcode_by_name_hashcode(self, name_hashcode, content_hashcode):
        # 根据name_hashcode修改content_hashcode  skywhat
        offset=hash_algorithm.get_hash_offset(name_hashcode)
        node=self.hash_list[offset]
        while node is not None and node.name_hashcode!=name_hashcode:
            node=node.next_node
        node.content_hashcode=content_hashcode


class FileHashNode(object):
    def __init__(self, sync_path, relative_path):
        self.path = relative_path  # path为相对路径
        self.next_node = None  # 下一节点
        self.name_hashcode = hash_algorithm.get_name_hashcode(self.path)  # 文件名hash值
        self.content_hashcode = hash_algorithm.get_content_hashcode(
            path.change_relative_path_to_absolute_path(sync_path, relative_path))  # 文件内容hash值

    def set_next_node(self, node):
        self.next_node = node

    def get_next_node(self):
        return self.next_node

    def get_name_hashcode(self):
        return self.name_hashcode

    def set_name_hashcode(self, path):
        self.name_hashcode = hash_algorithm.get_name_hashcode(path)

    def get_content_hashcode(self):
        return self.content_hashcode

    def set_content_hashcode(self, sync_path, relative_path):
        self.content_hashcode = hash_algorithm.get_content_hashcode(
            path.change_relative_path_to_absolute_path(sync_path, relative_path))

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    # 判断该节点的content_hash是否和传入的节点相同 skywhat
    # 若相同，返回True，不相同，返回False
    def is_equal_content_hash(self, node):
        if self.name_hashcode==node.name_hashcode and self.content_hashcode==node.content_hashcode:
            return True
        else:
            return False


#  遍历本地目录，填充一个sync_hash数组链表 返回一个填满的sync_hash数组链表 skywhat
def fill_sync_hash_list(sync_hash_list):
    path_list=path.get_all_file_path(path.local_path)
    for relative_path in path_list:
        node=FileHashNode(path.local_path,relative_path)
        sync_hash_list.insert(node)
    return sync_hash_list
