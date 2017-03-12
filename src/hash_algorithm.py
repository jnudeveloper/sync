#!/usr/bin/env python
#coding=utf-8
import hashlib
import math

sync_hash_length=4096

#计算文件名的在sync_hash中的位置
def Name_Hash(fname):
    m = hashlib.md5()
    m.update(fname)
    random_char_num=math.log(sync_hash_length,16)
    hashprint=m.hexdigest()[-int(random_char_num):]
    offset=int(hashprint,16) #该文件在sync_hash 中的位置
    return offset


#计算文件的MD5值 32位16进制
def Content_Hash(fname):
    def read_chunks(fh):
        fh.seek(0)
        chunk=fh.read(8096)
        while chunk:
            yield chunk
            chunk=fh.read(8096)
        else:
            fh.seek(0)

    m=hashlib.md5()
    with open(fname,"rb") as fh:
        for chunk in read_chunks(fh):
            m.update(chunk)
    return m.hexdigest()