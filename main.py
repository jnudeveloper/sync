# coding:utf-8
def valid_udisk_path(path):
    # 所有的路径都必须可读可写（也可以再后面再检查）
    # 对于情况1和3，如果路径存在且u盘下的这个目录已经初始化测返回True，否则返回False
    # 对于情况2和4，如果该路径存在则返回True，否则返回False
    if 1 == 1:
        return True
    else:
        return False


def valid_local_path(path):
    # 所有的路径都必须可读可写（也可以再后面再检查）
    # 对于情况1和3，如果路径存在且u盘下的这个目录已经初始化测返回True，否则返回False
    # 对于情况2和4，如果该路径存在则返回True，否则返回False
    if 1 == 1:
        return True
    else:
        return False


def print_choice():
    print("请选择：")
    print("1.同步的双方都已经存在项目，开始同步")
    print("2.本地已经存在项目，U盘中还没有对应项目")
    print("3.U盘中已经存在项目，本地还没有对应项目")
    print("4.根据本地已经存在的数据创建同步项目")
    print("5.退出程序\n")


if __name__ == "__main__":
    print("欢迎使用xxx")
    # 给出提示信息
    print_choice()
    choice = int(raw_input("您的选择是 ： "))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print("您的输入有误，请重新选择!")
        print_choice()
        choice = raw_input("您的选择是 ： ")

    # 若选择1
    if choice == 1:
        print("您选择了 1 ")
        uPath = raw_input("请输入U盘目录：")
        # （检查有效性后进入下一步）
        while not valid_udisk_path(uPath):
            uPath = raw_input("您输入的路径无效 ，请检查后重新输入U盘目录：")

        localPath = raw_input("请输入本地目录: ")
        # （检查有效性后进入下一步）
        while not valid_local_path(localPath):
            localPath = raw_input("您输入的路径无效 ，请检查后重新输入本地目录：")

        u_to_local = raw_input("是否从U盘同步到本地？（y/n）: ")
        while u_to_local != 'y' and u_to_local != 'Y' and u_to_local != 'n' and u_to_local != 'N':
            u_to_local = raw_input("是否从U盘同步到本地？（y/n）: ")
        if u_to_local == 'y'or u_to_local == 'Y':
            # 从U盘同步到本地
            print("从U盘同步到本地")
        elif u_to_local == 'n'or u_to_local == 'N':
            # 直接进入下一步
            pass

        local_to_u = raw_input("是否从本地同步到U盘？（y/n）: ")
        while local_to_u != 'y' and local_to_u != 'Y' and local_to_u != 'n' and local_to_u != 'N':
            local_to_u = raw_input("是否从本地同步到U盘？（y/n）: ")
        if local_to_u == 'y'or local_to_u == 'Y':
            # 从本地同步到U盘
            print("从本地同步到U盘")
        elif local_to_u == 'n'or local_to_u == 'N':
            # 直接进入下一步
            pass

        del_diff = raw_input("是否删除U盘上与本地不一致的数据?（y/n）: ")
        while del_diff != 'y' and del_diff != 'Y' and del_diff != 'N' and del_diff != 'n':
            del_diff = raw_input("是否删除U盘上与本地不一致的数据?（y/n）: ")
        if del_diff == 'y' or del_diff == 'Y':
            # 删除U盘上与本地不一致的数据
            print("删除U盘上与本地不一致的数据")
        elif del_diff == 'n'or del_diff == 'N':
            # 结束程序
            print("退出程序")
            exit()

    # 若选择2
    elif choice == 2:
        print("2")

    # 若选择3
    elif choice == 3:
        print("3")

    # 若选择4
    elif choice == 4:
        print("4")

    # 若选择5
    elif choice == 5:
        print("退出程序")
        exit()
