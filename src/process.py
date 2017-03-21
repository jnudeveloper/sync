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
        path.local_path = path.get_valid_local_path_with_project()
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # TODO 初始化diff数组 shiweihua
        # TODO 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
        # TODO 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
        # TODO 遍历比较sync_hash_local和sync_hash_udisk，得到数组diff、sync_hash_udisk、sync_hash_local 看增量pull流程图 shiweihua
        # TODO 根据diff数组，把u盘对应的文件覆盖本地的文件，同时把U盘上的该文件删除 shiweihua
        # TODO 根据现在的sync_hash_udisk， 把U盘新增的文件复制到本地， 同时把U盘上的该文件删除 shiweihua
        # TODO 根据现在的sync_hash_local， 在本地上删除U盘没有的文件 shiweihua
        # TODO 把U盘的.synchash文件复制到本地 shiweihua
        exit()
    elif num == 2:  # 增量push
        # 获取路径
        path.local_path = path.get_valid_local_path_with_project()
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # TODO 初始化数组： add_in_local、 diff shiweihua
        # TODO 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
        # TODO 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
        # TODO 递归扫描本地同步目录 得到数组diff、sync_hash_udisk、sync_hash_local 看增量push流程图 shiweihua
        # TODO 根据diff数组， 把本地对应的文件覆盖U盘的文件 shiweihua
        # TODO 同时修改sync_hash_udisk上相应节点中的content_hash shiweihua
        # TODO 根据add_in_local数组， 把本地新增的文件复制到U盘 shiweihua
        # TODO 遍历sync_hash_udisk， 如果该节点存在， 则不做任何操作否则把新增的节点添加到sync_hash_udisk上 shiweihua
        # TODO 根据sync_hash_local（delete_in_local） 数组，删除U盘上的文件 shiweihua
        # TODO 同时删除sync_hash_udisk上的相应节点（如果没有这个节点就不做任何操作） shiweihua
        # TODO 把sync_hash_udisk序列化到本地和U盘上的.synchash文件
        exit()
    elif num == 3:  # 全量pull
        # 获取路径
        path.local_path = path.get_valid_local_path()  # TODO 要空文件夹，看要不要加函数 liguoxiong
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # TODO 将U盘的所有文件同步到本地 shiweihua
        # TODO 将U盘的.synchash文件复制到本地 shiweihua
        exit()
    elif num == 4:  # 全量push
        # 获取路径
        path.local_path = path.get_valid_local_path_with_project()
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # TODO 本地项目初始化  见本地项目初始化流程图 shiweihua
        # TODO 将本地的所有文件复制到U盘 shiweihua
        # TODO 将本地的.synchash文件复制到U盘 shiweihua
        exit()
    elif num == 5:  # 手动删除U盘上的全量目录
        # 获取路径
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # TODO 检查U盘上是否已经有全量目录 shiweihua
        # TODO 如果有则删除U盘上的全量目录 shiweihua
        # TODO 如果没有就提示没有全量目录，然后不做将U盘的所有文件同任何操作 shiweihua
        exit()
    elif num == 6:  # 初始化本地已有的项目
        # TODO 请输入本地目录：（该目录要满足： 有效性、 不存在项目） liguoxiong
        # TODO 本地项目初始化  见本地项目初始化流程图 shiweihua
        exit()
    elif num == 7:  # 全量push
        # TODO 请输入U盘目录：（该目录要满足： 有效性、 空文件、 不存在项目） liguoxiong
        # TODO 在U盘上新建.sync文件夹， 在文件夹.sync中新建.synchash空文件 shiweihua
        # TODO 初始化一个sync_hash数组链表，序列化到U盘的.sync文件夹下的.synchash文件中
        exit()
