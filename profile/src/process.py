# coding=utf-8
# 流程的具体细节
import prompt
import path
import hash_algorithm
import serialize
import os
import sync
import shutil
import synchash


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
            if num == 1 or num == 2 or num == 3 \
                    or num == 4 or num == 5 or num == 6 or num == 7:
                break
            elif num == 8:
                exit()
            else:
                # 输入不是数字1-7时，提示再次输入
                num = raw_input(prompt.prompt_choose_again)

    if num == 1:  # 增量pull
        # 获取路径
        path.local_path = path.get_valid_path_with_project(prompt.prompt_local_path)
        path.udisk_path = path.get_valid_path_with_project_same_name(prompt.prompt_udisk_path)
        sync.incrementally_pull()
        print "执行增量pull完成，程序正常退出！"
        exit()
    elif num == 2:  # 增量push
        # 获取路径
        path.local_path = path.get_valid_path_with_project(prompt.prompt_local_path)
        path.udisk_path = path.get_valid_path_with_project_same_name(prompt.prompt_udisk_path)
        sync.incrementally_push()
        print "执行增量push完成，程序正常退出！"
        exit()
    elif num == 3:  # 全量pull
        # 获取路径
        path.local_path = path.get_valid_path_with_path_empty(prompt.prompt_local_path)
        path.udisk_path = path.get_valid_path_with_project_same_name_and_all_the_project(prompt.prompt_udisk_path)
        # 将U盘.sync目录下的同步目录同步到本地并将U盘的.synchash文件复制到本地 shiweihua
        sync.fully_pull(path.udisk_path, path.local_path)
        print "执行全量pull完成，程序正常退出！"
        exit()
    elif num == 4:  # 全量push
        # 获取路径
        path.local_path = path.get_valid_path_with_project(prompt.prompt_local_path)
        path.udisk_path = path.get_valid_path_with_project_same_name(prompt.prompt_udisk_path)
        # 本地项目初始化  见本地项目初始化流程图 shiweihua
        sync.init_local()
        # 将本地的所有文件复制到U盘的全量目录下 shiweihua
        sync.fully_push(path.local_path, path.udisk_path)
        print "执行全量push完成，程序正常退出！"
        exit()
    elif num == 5:  # 手动删除U盘上的全量目录
        # 获取路径
        path.udisk_path = path.get_valid_path_with_project(prompt.prompt_udisk_path)
        # 检查U盘上是否已经有全量目录 shiweihua
        if os.path.exists(path.udisk_path + os.sep + ".sync" + os.sep + ".all"):
            # 如果有则删除U盘上的全量目录 shiweihua
            shutil.rmtree(path.udisk_path + os.sep + ".sync" + os.sep + ".all")
            print "删除全量目录成功，程序正常退出！"
        else:
            # 如果没有就提示没有全量目录，然后不做任何操作 shiweihua
            print "U盘上并没有全量目录！程序正常退出！"
        exit()
    elif num == 6:  # 初始化本地已有的项目
        # 获取路径
        # 输入本地目录（该目录要满足： 有效性、 不存在项目）
        path.local_path = path.get_valid_path_with_project_is_not_exists(prompt.prompt_local_path)
        # 本地项目初始化  见本地项目初始化流程图 shiweihua
        sync.init_local()
        print "本地项目初始化完成，程序正常退出！"
        exit()
    elif num == 7:  # 初始化U盘
        # 获取路径
        # 输入U盘目录（该目录要满足： 有效性、 文件夹为空）
        path.udisk_path = path.get_valid_path_with_path_empty(prompt.prompt_udisk_path)
        # 初始化U盘
        sync.init_udisk()
        print "U盘初始化完成，程序正常退出！"
        exit()
