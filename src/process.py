# coding=utf-8
# 流程的具体细节
import prompt
import path
import sync


# 脚本开始时获取用户输入，进入不同的状态
def run():
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
        path.local_path = path.get_valid_local_path_with_project()
        path.usb_path = path.get_valid_usb_path_with_project()
        # !反序列化.synchash文件得到哈希数组链表sync_hash
        # !遍历sync_hash,将每个FileHash中flag置0
        # !初始化全局数组diff，no_in_local,no_in_udisk
        # !递归扫描同步目录并计算diff，no_in_local,no_in_udisk中的元素
        # !选择push/pull
        # !执行push/pull
        # 执行safe_exit(),反序列化sync_hash并结束程序
        safe_exit()
    elif num == 2:
        # 本地存在项目，U盘不存在项目
        # 获取路径
        path.local_path = path.get_valid_local_path_with_project()
        path.usb_path = path.get_valid_usb_path()
        # 初始化U盘目录
        sync.init_project(path.usb_path)
        # !new一个哈希数组链表sync_hash
        # !递归扫描本地同步目录，将每一个扫描到的文件加入到sync_hash,把并把该文件同步到U盘
        # 执行safe_exit(),反序列化sync_hash并结束程序
        safe_exit()
    elif num == 3:
        # U盘存在项目，本地不存在项目
        # 获取路径
        path.local_path = path.get_valid_local_path()
        path.usb_path = path.get_valid_usb_path_with_project()
        # 初始化本地目录
        sync.init_project(path.local_path)
        # !将U盘上的.synchash文件反序列化为哈希数组链表sync_hash
        # !遍历sync_hash,对每一个FileHash对象将U盘中的相应文件同步到本地
        # 可以直接结束文件，不需要将sync_hash反序列化
        print("程序正常结束\n")
        exit(0)
    elif num == 4:
        # 本地和U盘都不存在项目
        # 获取路径
        path.local_path = path.get_valid_local_path()
        path.usb_path = path.get_valid_usb_path()
        # 初始化本地目录
        sync.init_project(path.local_path)
        # 初始化U盘目录
        sync.init_project(path.usb_path)
        # !new一个哈希数组链表sync_hash
        # !递归扫描本地同步目录，将每一个扫描到的文件加入到sync_hash,把并把该文件同步到U盘
        # 执行safe_exit(),反序列化sync_hash并结束程序
        safe_exit()


# 反序列化sync_hash并结束程序
def safe_exit():
    # !反序列化sync_hash
    print("程序正常结束\n")
    exit(0)
