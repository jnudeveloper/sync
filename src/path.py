# coding=utf-8
# 路径（目录）的操作：判断路径是否有效等
import prompt
import os

local_path = ''
udisk_path = ''


# 判断路径是否存在项目（该路径下存在文件 .synchash）
# 前提：目录存在、可读、可写
# udisk路径还要判断是否同名
# 有效返回True，无效返回False
def is_path_valid_and_has_project(path, device_type="local"):
    path_valid = True
    if not is_path_valid(path, device_type):
        path_valid = False
    elif not is_project_exists(path):
        print prompt.prompt_sync_hash_file_is_not_exist
        # .synchash文件不存在
        path_valid = False
    return path_valid


# 判断路径是否有效
# 目录存在、可读、可写
# udisk路径还要判断是否同名
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
    elif device_type == "udisk" and (not is_current_dir_same(path)):
        print prompt.prompt_path_name_is_not_same
        path_valid = False
    return path_valid


# 判断文件夹是否为空
# 为空：返回True， 不为空：返回False
# author 李国雄
def is_path_empty(path):
    if os.listdir(path):
        return False
    return True


# 判断项目是否存在：存在.sync文件夹，.sync文件夹中存在.synchash文件
# 项目存在：返回True， 不存在：返回False
# author 李国雄
def is_project_exists(path):
    if not os.path.exists(path + os.path.sep + ".sync"):
        return False
    if not os.path.isfile(path + os.path.sep + ".sync" + os.path.sep + ".synchash"):
        return False
    return True


# 判断目录是否可写
# 可写：返回 True ， 不可写：返回  False
# author 李国雄
def is_writeable(path):
    # TODO 方法未测试 liguoxiong
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        return True
    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        return False


# 判断目录是否可读
# 可读：返回 True  ，  不可读：返回  False
# author 李国雄
def is_readable(path):
    # TODO 方法未测试 liguoxiong
    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        return True
    return False


# 判断udisk路径和本地路径的当前目录是否同名
# author 李国雄
def is_current_dir_same(udisk_path_name):
    local_path_name = delete_last_slash(local_path)
    local_path_basename = os.path.basename(local_path_name)
    udisk_path_name = delete_last_slash(udisk_path_name)
    udisk_path_basename = os.path.basename(udisk_path_name)
    if local_path_basename == udisk_path_basename:
        return True
    return False


# 获取本地目录
# 目录存在、可读、可写
# TODO 路径不能有文件，如果有文件要提示，重新输入 liguoxiong
def get_valid_local_path():
    return get_valid_path(raw_input(prompt.prompt_local_path), "local")


# 获取U盘目录
# 目录存在、可读、可写
# 文件夹名称和之请输入的本地文件夹名称一致
# TODO 路径不能有文件，如果有文件要提示，重新输入  liguoxiong
def get_valid_udisk_path():
    return get_valid_path(raw_input(prompt.prompt_udisk_path), "udisk")


# 获取有效的本地目录（目录存在、可读、可写）
# 路径存在项目（该路径下存在.sync文件夹，.sync文件夹中有.synchash文件）
# TODO 李国雄
def get_valid_local_path_with_project():
    return get_valid_path_with_project(raw_input(prompt.prompt_local_path), "local")


# 获取有效的U盘目录（目录存在、可读、可写）
# 路径存在项目（该路径下存在.sync文件夹，.sync文件夹中有.synchash文件）
# 文件夹名称和之请输入的本地文件夹名称一致
# TODO 李国雄
def get_valid_udisk_path_with_project():
    return get_valid_path_with_project(raw_input(prompt.prompt_udisk_path), "udisk")


# TODO 获取本地目录  liguoxiong
# TODO 注意：目录可以有文件  liguoxiong
# 目录存在、可读、可写、路径存在项目（该路径下存在文件 .synchash）
def get_valid_local_path_even_had_file():
    # TODO liguoxiong
    pass


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


# 把本地的绝对路径变成相对路径
# author 李国雄
# 如果根目录sync_path为：/usr/bin 、绝对路径为：/usr/bin/path/test/ ， 则得到的相对路径为：path/test(前后都没有分隔符)
def change_absolute_path_to_relative_path(sync_path, absolute_path):
    sync_path = add_last_slash(sync_path)
    relative_path = absolute_path[len(sync_path):]
    return delete_last_slash(relative_path)


# 把本地的相对路径变成绝对路径
# author 李国雄
# 如果根目录sync_path为：/usr/bin 、相对路径为：/path/test/ ， 则得到的绝对路径为：/usr/bin/path/test(后面没有分隔符)
def change_relative_path_to_absolute_path(sync_path, relative_path):
    if relative_path.startswith(os.sep) or relative_path.startswith("/") or relative_path.startswith("\\"):
        relative_path = relative_path[1:]
    relative_path = delete_last_slash(relative_path)
    absolute_path = delete_last_slash(sync_path) + os.sep + relative_path
    return absolute_path


# 去掉路径的最后的斜杠(不管数量多少，全部去掉)。如果路径最后没有斜杠，则不再操作，直接返回原路径
# author 李国雄
def delete_last_slash(path):
    if path.endswith(os.sep) or path.endswith("/") or path.endswith("\\"):
        return os.path.dirname(path)
    return path


# 路径的最后增加路径分隔符
# author 李国雄
def add_last_slash(path):
    path = delete_last_slash(path)
    return path + os.sep


# @author shiwehua
#  遍历给出的目录，以数组形式返回目录下的所有文件的路径
def traverse_sync(path):
    file_path_arr = []
    for root, dirs, files in os.walk(path):
        for files_path in files:
            file_path_arr.append(os.path.join(root, files_path))
    return file_path_arr


# @author shiwehua
# 获取同步目录下除.sync目录下的所有文件路径，返回一个所有路径的数组
def get_all_file_path(sync_path):
    file_path_arr = []
    folders = os.listdir(sync_path)
    for folder in folders:
        if folder == ".sync":
            pass
        elif os.path.isfile(sync_path + os.sep + folder):
            file_path_arr.append(sync_path + os.sep + folder)
        elif os.path.isdir(sync_path + os.sep + folder):
            file_path_arr.extend(traverse_sync(sync_path + os.sep + folder))
    return file_path_arr
