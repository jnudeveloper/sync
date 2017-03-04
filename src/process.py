# coding=utf-8
# 流程的具体细节
import prompt
import path


# 脚本开始时获取用户输入，进入不同的状态
def init_input():
    print prompt.prompt_init
    num = raw_input(prompt.prompt_choose)
    while True:
        if not num.isdigit():
            # 输入不是数字字符时，提示再次输入
            num = raw_input(prompt.prompt_choose_again)
        else:
            # 输入为数字字符，字符转换成数
            num = int(num)
            if num == 1 or num == 2 or num == 3 or num == 4:
                # 获取路径
                get_local_path()
                get_usb_path()
                break
            elif num == 5:
                exit()
            else:
                # 输入不是数字1-5时，提示再次输入
                num = raw_input(prompt.prompt_choose_again)
    if num == 1:
        print "您选择了 1 "
        # TODO
    elif num == 2:
        print "您选择了 2 "
        # TODO
    elif num == 3:
        print "您选择了 3 "
        # TODO
    elif num == 4:
        print "您选择了 4 "
        # TODO


# 获取本地目录
def get_local_path():
    local_path = raw_input(prompt.prompt_local_path)
    path.get_valid_path(local_path)


# 获取U盘目录
def get_usb_path():
    usb_path = raw_input(prompt.prompt_usb_path)
    path.get_valid_path(usb_path)

