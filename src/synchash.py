#!/usr/bin/python
# coding=utf-8
# .synchash 文件的hash指纹信息
import hashlib

class NameHash(object):
	def __init__(self,data):
		self.data=data  # data为文件名字符串
		self.next_node=None
		self.flag=0
		self.hashcode=0
		self.contentHash=ContentHash(NULL)

	def set_next(self,nameHash):
		self.next_node=nameHash

	def get_next(self):
		return self.next_node

	def set_hashcode(self,data):
		self.hashcode=Hash(data) # Hash 某种hash 函数

	def get_hashcode(self):
		return hashcode

	def get_data(self):
		return self.data

	def data_equals(self,data):
		return self.data==data

	def set_flag(self,flag):
		self.flag=flag;#初始化flag=0  0：本地无此文件 1：本地文件与U盘一致  2：本地文件与U盘不一致  3：U盘无此文件

	def get_flag(self):
		return self.flag

class ContentHash(object):
	def __init__(self,data):
		self.data=data
		self.hashcode=0

	def set_hashcode(self,data):
		self.hashcode=Hash(data)# Hash 某种hash 函数

	def get_hashcode(self):
		return self.hashcode

	def get_path(self):
		return path
