# coding=utf-8
# 流程的具体细节
import prompt
import path
import sync


# 脚本开始时获取用户输入，进入不同的状态
def init_input():
    print prompt.prompt_init
    num = raw_input(prompt.prompt_init_choose)
    # 获取用户输入，直到输入正确
    while True:
        if not num.isdigit():
            # 输入不是数字字符时，提示再次输入
            num = raw_input(prompt.prompt_choose_again)
        else:
            # 输入为数字字符，字符转换成数
            num = int(num)
            if num == 1 or num == 2 or num == 3 or num == 4:
                break
            elif num == 5:
                exit()
            else:
                # 输入不是数字1-5时，提示再次输入
                num = raw_input(prompt.prompt_choose_again)
    if num == 1:
        # 本地和U盘都存在项目
        # 获取路径
        path.local_path = path.get_valid_local_path()
        path.usb_path = path.get_valid_usb_path()
    elif num == 2:
        # 本地存在项目，U盘不存在项目
        # 获取路径
        path.local_path = path.get_valid_local_path()
        path.usb_path = path.get_usb_path()
        sync.init_usb()
    elif num == 3:
        # U盘存在项目，本地不存在项目
        # 获取路径
        path.local_path = path.get_local_path()
        path.usb_path = path.get_valid_usb_path()
        sync.init_local()
    elif num == 4:
        # 本地和U盘都不存在项目
        # 获取路径
        path.local_path = path.get_local_path()
        path.usb_path = path.get_usb_path()
        sync.init_usb()
        sync.init_local()
    local_to_usb_choose()
    usb_to_local_choose()


# 选择是否把U盘的数据传到本地
def usb_to_local_choose():
    choose = raw_input(prompt.prompt_usb_to_local_choose)
    while choose not in ('y', 'Y', 'n', 'N'):
        choose = raw_input(prompt.prompt_choose_again)
    else:
        if choose == 'y' or choose == 'Y':
            sync.usb_to_local()


# 选择是否把本地的数据传到U盘
def local_to_usb_choose():
    choose = raw_input(prompt.prompt_usb_to_local_choose)
    while choose not in ('y', 'Y', 'n', 'N'):
        choose = raw_input(prompt.prompt_choose_again)
    else:
        if choose == 'y' or choose == 'Y':
            sync.local_to_usb()

