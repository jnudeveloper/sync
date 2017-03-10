# coding=utf-8
# 路径（目录）的操作：判断路径是否有效等
import prompt
import os

local_path = ''
usb_path = ''


# 判断路径是否有效
# 有效：目录存在、可读、可写、该路径下存在文件 synchash
# 有效返回True，无效返回False
def is_path_valid(path):
    path_valid = True
    if not os.path.exists(path):
        # 目录不存在
        print prompt.prompt_path_is_not_exist
        path_valid = False
    elif not is_readable(path):
        print prompt.prompt_path_is_not_readable
        # 目录不可读
        path_valid = False
    elif not is_writeable(path):
        print prompt.prompt_path_is_not_writeable
        # 目录不可写
        path_valid = False
    elif not is_sync_hash_exist(path):
        print prompt.prompt_sync_hash_file_is_not_exist
        # synchash文件不存在
        path_valid = False
    return path_valid


# 判断synchash文件是否存在
# synchash 存在：返回True， 不存在：返回False
def is_sync_hash_exist(path):
    return os.path.isfile(path + os.path.sep + "synchash.txt")


# 判断目录是否可写
# 可写：返回 True ， 不可写：返回  False
def is_writeable(path, check_parent=False):
    # TODO
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        return True
    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        return False
    if check_parent is False:
        return False
    parent_dir = os.path.dirname(path)
    if not os.access(parent_dir, os.F_OK):
        return False
    return os.access(parent_dir, os.W_OK)


# 判断目录是否可读
# 可读：返回 True  ，  不可读：返回  False
def is_readable(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        return True
    return False


# 获取本地目录
def get_local_path():
    return get_path(raw_input(prompt.prompt_local_path))


# 获取U盘目录
def get_usb_path():
    return get_path(raw_input(prompt.prompt_usb_path))


# 获取有效的本地目录
def get_valid_local_path():
    return get_valid_path(raw_input(prompt.prompt_local_path))


# 获取有效的U盘目录
def get_valid_usb_path():
    return get_valid_path(raw_input(prompt.prompt_usb_path))


# 循环获取路径，直到路径存在
def get_path(path):
    while not os.path.exists(path):
        # 路径不存在时，继续输入
        print prompt.prompt_path_is_not_exist
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return path


# 循环获取路径，直到路径有效
def get_valid_path(path):
    while not is_path_valid(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return path
