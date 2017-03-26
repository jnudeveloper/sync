# coding=utf-8
# 路径（目录）的操作：判断路径是否有效等
import prompt
import os

local_path = ''
udisk_path = ''


# 路径有效 和 路径存在项目
# 目录存在、可读、可写、存在项目
# 符合要求返回True，否则返回False
# author 李国雄
def is_path_valid_and_is_path_empty(path):
    path_valid = True
    if not is_path_valid(path):
        path_valid = False
    elif not is_path_empty(path):
        print prompt.prompt_path_is_not_empty
        path_valid = False
    return path_valid


# 路径有效 和 路径存在项目 和 目录同名
# 目录存在、可读、可写、存在项目、同名
# 符合要求返回True，否则返回False
# author 李国雄
def is_path_valid_and_is_project_exists_and_is_dir_same(path):
    path_valid = True
    if not is_path_valid_and_is_project_exists(path):
        path_valid = False
    elif not is_current_dir_same(path, local_path):
        print prompt.prompt_path_name_is_not_same
        path_valid = False
    return path_valid


# 路径有效 和 路径存在项目
# 目录存在、可读、可写、存在项目
# 符合要求返回True，否则返回False
# author 李国雄
def is_path_valid_and_is_project_exists(path):
    path_valid = True
    if not is_path_valid(path):
        path_valid = False
    elif not is_project_exists(path):
        print prompt.prompt_sync_hash_file_is_not_exists
        path_valid = False
    return path_valid


# 路径有效 和 路径存在项目 和 目录同名 和 存在全量目录
# 目录存在、可读、可写、存在项目、目录同名、存在全量目录
# 符合要求返回True，否则返回False
# author 李国雄
def is_path_valid_and_is_project_exists_and_is_dir_sameand_has_all_the_project(path):
    path_valid = True
    if not is_path_valid_and_is_project_exists_and_is_dir_same(path):
        path_valid = False
    elif not is_path_have_all_the_project(path):
        print prompt.prompt_do_not_have_all_the_project
        path_valid = False
    return path_valid


# 路径有效 和 路径不存在项目
# 目录存在、可读、可写、不存在项目
# 符合要求返回True，否则返回False
# author 李国雄
def is_path_valid_and_is_project_not_exists(path):
    path_valid = True
    if not is_path_valid(path):
        path_valid = False
    elif is_project_exists(path):
        print prompt.prompt_sync_hash_file_is_exists
        path_valid = False
    return path_valid


# 判断路径是否有效
# 目录存在、可读、可写
# 有效返回True，无效返回False
# author 李国雄
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
    return path_valid


# 判断文件夹是否为空
# 为空返回：True， 不为空返回：False
# author 李国雄
def is_path_empty(path):
    if os.listdir(path):
        return False
    return True


# 判断文件夹是否含有全量目录
# 存在返回：True， 不存在返回：False
# author 李国雄
def is_path_have_all_the_project(path):
    if not os.path.exists(path + os.path.sep + ".sync" + os.path.sep + ".all"):
        return False
    return True


# 判断项目是否存在（存在.sync文件夹，.sync文件夹中存在.synchash文件）
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
def is_writeable(path):
    # TODO 方法未测试 liguoxiong
    if os.access(path, os.F_OK) and os.access(path, os.W_OK):
        return True
    if os.access(path, os.F_OK) and not os.access(path, os.W_OK):
        return False


# 判断目录是否可读
# 可读：返回 True  ，  不可读：返回  False
def is_readable(path):
    # TODO 方法未测试 liguoxiong
    if os.access(path, os.F_OK) and os.access(path, os.R_OK):
        return True
    return False


# 判断udisk路径和本地路径的当前目录是否同名
# 同名返回：True ， 不同名返回：False
# author 李国雄
def is_current_dir_same(udisk_path_name, local_path_name):
    local_path_name = delete_last_slash(local_path_name)
    local_path_basename = os.path.basename(local_path_name)
    udisk_path_name = delete_last_slash(udisk_path_name)
    udisk_path_basename = os.path.basename(udisk_path_name)
    if local_path_basename == udisk_path_basename:
        return True
    return False


# 循环获取路径，直到路径有效和存在项目
# 目录存在、可读、可写、路径存在项目
# author 李国雄
def get_valid_path_with_project(prompt_str):
    path = raw_input(prompt_str)
    while not is_path_valid_and_is_project_exists(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return delete_last_slash(path)


# 循环获取路径，直到路径有效、存在项目和同名
# 目录存在、可读、可写、路径存在项目、同名
# author 李国雄
def get_valid_path_with_project_same_name(prompt_str):
    path = raw_input(prompt_str)
    while not is_path_valid_and_is_project_exists_and_is_dir_same(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return delete_last_slash(path)


# 循环获取路径，直到路径有效、路径为空
# 目录存在、可读、可写、路径为空
# author 李国雄
def get_valid_path_with_path_empty(prompt_str):
    path = raw_input(prompt_str)
    while not is_path_valid_and_is_path_empty(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return delete_last_slash(path)


# 循环获取路径，直到路径有效、不存在项目（目录不一定为空）
# 目录存在、可读、可写、不存在项目（目录不一定为空）
# author 李国雄
def get_valid_path_with_project_is_not_exists(prompt_str):
    path = raw_input(prompt_str)
    while not is_path_valid_and_is_project_not_exists(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return delete_last_slash(path)


# 路径有效 和 路径存在项目 和 目录同名 和 存在全量目录
# 目录存在、可读、可写、存在项目、目录同名、存在全量目录
# author 李国雄
def get_valid_path_with_project_same_name_and_all_the_project(prompt_str):
    path = raw_input(prompt_str)
    while not is_path_valid_and_is_project_exists_and_is_dir_sameand_has_all_the_project(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_do_not_have_all_the_project)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
        return delete_last_slash(path)


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
    return delete_last_slash(absolute_path)


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
# review一下看有没有错 shiweihua （所以有没有问题？ by shiweihua）(可以了，没问题  by 李国雄)
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
