# coding=utf-8
# 路径（目录）的操作：判断路径是否有效等
import prompt


# 判断路径是否有效
# 有效返回True，无效返回False
def is_path_valid(path):
    # TODO 判断路径是否有效
    return True


# 循环获取路径，直到路径有效
def get_valid_path(path):
    while not is_path_valid(path):
        # 路径无效时，继续输入
        path = raw_input(prompt.prompt_error_path)
    else:
        # 路径有效时, 提示输入成功
        print prompt.prompt_path_success
