# coding=utf-8
# 提示语汇总

# 脚本开始时的提示语
prompt_init = """
欢迎使用xxx
1. 本地和U盘都存在项目，开始同步
2. 本地存在项目，U盘不存在项目
3. U盘存在项目，本地不存在项目
4. 本地和U盘都不存在项目
5. 退出程序
"""

# 提示用户输入
prompt_init_choose = """请选择要进行的操作： """

# 用户输入错误时提示再次输入
prompt_choose_again = """您的输入有误，请重新选择: """

# 提示输入本地目录
prompt_local_path = """请输入本地目录："""

# 提示输入U盘目录
prompt_usb_path = """请输入U盘目录："""

# 路径无效，提示重新输入：
prompt_error_path = """您输入的路径无效，请检查后重新输入目录："""

# 本地目录输入成功
prompt_path_success = """目录输入成功！"""

# 选择是否从U盘同步到本地
prompt_usb_to_local_choose = """是否从U盘同步到本地？（y/n）： """

# 选择是否从本地同步到U盘
prompt_local_to_usb_choose = """是否从本地同步到U盘？（y/n）： """
