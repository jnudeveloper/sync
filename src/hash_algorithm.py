#!/usr/bin/env python
# coding=utf-8
import hashlib
import math

sync_hash_length = 4096


# 计算文件名的哈希值
def Name_Hash(fname):
    hash_md5 = hashlib.md5(fname)
    return hash_md5.hexdigest()


# 根据文件名计算文件在哈希数组中的偏移量
def Hash_Offset(fname):
    fname_md5 = Name_Hash(fname)
    random_char_num = math.log(sync_hash_length,16)
    hashprint = fname_md5[-int(random_char_num):]
    offset = int(hashprint, 16)  # 该文件在sync_hash 中的位置
    return offset


# 计算文件的MD5值 32位16进制
def Content_Hash(fname):
    def read_chunks(fh):
        fh.seek(0)
        chunk = fh.read(8096)
        while chunk:
            yield chunk
            chunk = fh.read(8096)
        else:
            fh.seek(0)

    m = hashlib.md5()
    with open(fname, "rb") as fh:
        for chunk in read_chunks(fh):
            m.update(chunk)
    return m.hexdigest()
