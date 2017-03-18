#!/usr/bin/env python
# coding=utf-8
import hashlib
import math

hash_sub_string_length = 3
sync_hash_length = 16 ** hash_sub_string_length


# 计算文件名的哈希值
def get_name_hash(filename):
    hash_md5 = hashlib.md5(filename)
    return hash_md5.hexdigest()


# 根据文件名计算文件在哈希数组中的偏移量
def get_hash_offset(filename):
    filename_md5 = get_name_hash(filename)
    random_char_num = math.log(sync_hash_length, 16)
    hash_print = filename_md5[-int(random_char_num):]
    offset = int(hash_print, 16)  # 该文件在sync_hash 中的位置
    return offset


# 计算文件的MD5值 32位16进制
def get_content_hash(filename):
    m = hashlib.md5()
    with open(filename, "rb") as file_stream:
        for chunk_item in read_chunks(file_stream):
            m.update(chunk_item)
    return m.hexdigest()


# 读取文件流
def read_chunks(file_stream):
    file_stream.seek(0)
    hash_chunk = file_stream.read(8096)
    while hash_chunk:
        yield hash_chunk
        hash_chunk = file_stream.read(8096)
    else:
        file_stream.seek(0)
