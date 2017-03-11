# coding=utf-8
# 路径（目录）的操作：判断路径是否有效等
import prompt
import os

local_path = ''
usb_path = ''


# 判断路径是否存在项目（该路径下存在文件 .synchash）
# 前提：目录存在、可读、可写
# usb路径还要判断是否同名
# 有效返回True，无效返回False
def is_path_valid_and_has_project(path, device_type="local"):
    path_valid = True
    if not is_path_valid(path, device_type):
        path_valid = False
    elif not is_sync_hash_exists(path):
        print prompt.prompt_sync_hash_file_is_not_exist
        # .synchash文件不存在
        path_valid = False
    return path_valid


# 判断路径是否有效
# 目录存在、可读、可写
# usb路径还要判断是否同名
# 有效返回True，无效返回False
def is_path_valid(path, device_type="local"):
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
    elif device_type == "usb" and (not is_current_dir_same(path)):
        print prompt.prompt_path_name_is_not_same
        path_valid = False
    return path_valid


# 判断.synchash文件是否存在
# .synchash 存在：返回True， 不存在：返回False
def is_sync_hash_exists(path):
    return os.path.isfile(path + os.path.sep + ".synchash")


# 判断目录是否可写
# 可写：返回 True ， 不可写：返回  False
def is_writeable(path):
    # TODO
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        return True
    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        return False


# 判断目录是否可读
# 可读：返回 True  ，  不可读：返回  False
def is_readable(path):
    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        return True
    return False


# 判断usb路径和本地路径的当前目录是否同名
def is_current_dir_same(path):
    local_path_dirname = os.path.dirname(local_path)
    usb_path_dirname = os.path.dirname(path)
    local_path_basename_with_sep = os.path.basename(local_path_dirname)
    usb_path_basename_with_sep = os.path.basename(usb_path_dirname)
    local_path_basename_without_sep = os.path.basename(local_path)
    usb_path_basename_without_sep = os.path.basename(path)
    if local_path.endswith(os.sep) \
            and path.endswith(os.sep) \
            and local_path_basename_with_sep == usb_path_basename_with_sep:
        return True
    if (not local_path.endswith(os.sep)) \
            and path.endswith(os.sep) \
            and local_path_basename_without_sep == usb_path_basename_with_sep:
        return True
    if local_path.endswith(os.sep) \
            and (not path.endswith(os.sep)) \
            and local_path_basename_with_sep == usb_path_basename_without_sep:
        return True
    if (not local_path.endswith(os.sep)) \
            and (not path.endswith(os.sep)) \
            and local_path_basename_without_sep == usb_path_basename_without_sep:
        return True
    return False


# 获取本地目录
# 目录存在、可读、可写
def get_valid_local_path():
    return get_valid_path(raw_input(prompt.prompt_local_path), "local")


# 获取U盘目录
# 目录存在、可读、可写
# 文件夹名称和之请输入的本地文件夹名称一致
def get_valid_usb_path():
    return get_valid_path(raw_input(prompt.prompt_usb_path), "usb")


# 获取有效的本地目录
# 目录存在、可读、可写、路径存在项目（该路径下存在文件 .synchash）
def get_valid_local_path_with_project():
    return get_valid_path_with_project(raw_input(prompt.prompt_local_path), "local")


# 获取有效的U盘目录
# 目录存在、可读、可写、路径存在项目（该路径下存在文件 .synchash）
# 文件夹名称和之请输入的本地文件夹名称一致
def get_valid_usb_path_with_project():
    return get_valid_path_with_project(raw_input(prompt.prompt_usb_path), "usb")


# 循环获取路径，直到路径有效
# 目录存在、可读、可写
def get_valid_path(path, device_type="local"):
    while not is_path_valid(path, device_type):
        # 路径不存在时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return path


# 循环获取路径，直到路径有效
# 目录存在、可读、可写、路径存在项目（该路径下存在文件 .synchash）
def get_valid_path_with_project(path, device_type="local"):
    while not is_path_valid_and_has_project(path, device_type):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return path
