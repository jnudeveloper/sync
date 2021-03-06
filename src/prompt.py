# coding=utf-8
# 提示语汇总

# 脚本开始时的提示语
prompt_init = """
欢迎使用xxx
1. 增量pull
2. 增量push
3. 全量pull
4. 全量push
5. 手动删除U盘上的全量目录
6. 初始化本地已有的项目
7. 初始化U盘
8. 退出程序
"""

# 提示用户输入
prompt_init_choose = """请选择要进行的操作： """

# 用户输入错误时提示再次输入
prompt_choose_again = """您的输入有误，请重新选择: """

# 提示输入本地目录
prompt_local_path = """请输入本地目录："""

# 提示输入U盘目录
prompt_udisk_path = """请输入U盘目录："""

# 提示重新输入路径：
prompt_error_path = """请检查后重新输入目录："""

# 路径不存在
prompt_path_is_not_exist = """输入的路径不存在！\n"""

# 路径不可读
prompt_path_is_not_readable = """输入的路径不可读！\n"""

# 路径不可写
prompt_path_is_not_writeable = """输入的路径不可写！\n"""

# 路径不存在项目，即未初始化
prompt_sync_hash_file_is_not_exists = """输入的路径不存在项目！\n"""

# 路径不存在项目，即未初始化
prompt_do_not_have_all_the_project = """输入的路径没有全量目录！\n"""

# 输入的路径已经存在项目
prompt_sync_hash_file_is_exists = """输入的路径已经存在项目! \n """

# udisk路径中文件夹名称和本地的不同
prompt_path_name_is_not_same = """u盘路径中文件夹名称和本地的不同！\n"""

# udisk路径中文件夹名称和本地的不同
prompt_path_is_not_empty = """本地目录应该为空，请选择一个空目录！\n"""

# 目录输入成功
prompt_path_success = """目录输入成功！\n"""
