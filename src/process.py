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
        path.local_path = path.get_valid_local_path_with_project()
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # 初始化diff数组 shiweihua
        diff = []
        # 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
        sync_hash_local = serialize.deserialize(path.local_path+os.sep+".sync"+os.sep+".synchash")
        # 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
        sync_hash_udisk = serialize.deserialize(path.udisk_path+os.sep+".sync"+os.sep+".synchash")
        # 遍历比较sync_hash_local和sync_hash_udisk，得到数组diff、sync_hash_udisk、sync_hash_local 看增量pull流程图 shiweihua
        for i in range(hash_algorithm.sync_hash_length):
            local_node = sync_hash_local[i]
            while local_node != None:
                temp_flag = 0
                udisk_node = sync_hash_udisk[i]
                while udisk_node != None:
                    udisk_name_hash = udisk_node.get_name_hashcode()
                    local_name_hash = local_node.get_name_hashcode()
                    if udisk_name_hash == local_name_hash:
                        # 两个节点的文件名hash相同
                        udisk_content_hash = udisk_node.get_content_hashcode()
                        local_content_hash = local_node.get_content_hashcode()
                        if udisk_content_hash != local_content_hash:
                            # 两个节点的文件名hash相同但文件内容hash不同，把udisk对应的节点放到diff数组中
                            diff.append(udisk_node)
                        local_node = local_node.get_next_node()
                        sync_hash_local.delete_by_name_hashcode(local_name_hash)
                        sync_hash_udisk.delete_by_name_hashcode(udisk_name_hash)
                        temp_flag = 1
                        break
                    udisk_node = udisk_node.get_next_node()
                if temp_flag == 1:
                    continue
                else:
                    local_node = local_node.get_next_node()
        # 根据diff数组，把u盘对应的文件覆盖本地的文件，同时把U盘上的该文件删除 shiweihua
        for diff_node in diff:
            sync.move_to_local(path.local_path, path.udisk_path, diff_node)
            sync.delete_from_udisk(path.udisk_path, diff_node)
        # 根据现在的sync_hash_udisk， 把U盘新增的文件复制到本地， 同时把U盘上的该文件删除 shiweihua
        for i in range(hash_algorithm.sync_hash_length):
            add_in_other = sync_hash_udisk[i]
            while add_in_other != None:
                sync.move_to_local(path.local_path, path.udisk_path, add_in_other)
                sync.delete_from_udisk(path.udisk_path, add_in_other)
                add_in_other = add_in_other.get_next_node()
        # 根据现在的sync_hash_local， 在本地上删除U盘没有的文件 shiweihua
        for i in range(hash_algorithm.sync_hash_length):
            delete_in_other = sync_hash_udisk[i]
            while delete_in_other != None:
                sync.delete_from_local(path.local_path, delete_in_other)
                delete_in_other = delete_in_other.get_next_node()
        # 把U盘的.synchash文件复制到本地 shiweihua
        shutil.copy2(path.udisk_path+os.sep+".sync"+os.sep+".synchash",
                     path.local_path+os.sep+".sync"+os.sep+".synchash")
        print "执行增量pull完成，程序正常退出！"
        exit()
    elif num == 2:  # 增量push
        # 获取路径
        path.local_path = path.get_valid_local_path_with_project()
        path.udisk_path = path.get_valid_udisk_path_with_project()
        # 初始化数组： add_in_local、 diff shiweihua
        add_in_local = []
        diff = []
        # 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
        sync_hash_local = serialize.deserialize(path.local_path+os.sep+".sync"+os.sep+".synchash")
        # 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
        sync_hash_udisk = serialize.deserialize(path.udisk_path + os.sep + ".sync" + os.sep + ".synchash")
        # 递归扫描本地目录，得到一个包含本地同步目录下所有文件路径的数组（.sync目录除外） shiweihua
        file_path_arr = path.get_all_file_path(path.local_path)
        # 根据file_path_arr数组计算diff、sync_hash_udisk、sync_hash_local 看增量push流程图 shiweihua
        for file in file_path_arr:
            # TODO 将绝对路径变成相对路径relative_path
            relative_path = "test"
            # 计算文件名hash
            name_hashcode = hash_algorithm.get_name_hashcode(relative_path)
            node_in_udisk = sync_hash_udisk.find_by_name_hashcode(name_hashcode)
            if node_in_udisk != None: #判断节点是否在sync_hash_udisk中
                # 如果在sync_hash_udisk中，计算文件内容hash
                content_hashcode = hash_algorithm.get_content_hashcode(relative_path)
                if content_hashcode != node_in_udisk.get_content_hashcode():
                    # 把该文件节点放到diff数组中
                    node = synchash.FileHashNode(relative_path)
                    diff.append(node)
            node_in_local = sync_hash_local.find_by_name_hashcode(name_hashcode)
            if node_in_local != None:  # 判断节点是否在sync_hash_local中
                # 如果在sync_hash_local中则从sync_hash_local中删除这个节点
                sync_hash_local.delete_by_name_hashcode(name_hashcode)
            else:
                # 如果不在sync_hash_local中则把扫描的文件节点放到add_in_local中
                node = synchash.FileHashNode(relative_path)
                add_in_local.append(node)
        # 根据diff数组,把本地对应的文件覆盖U盘的文件,同时修改sync_hash_udisk上相应节点中的content_hash shiweihua
        for diff_node in diff:
            sync.move_to_local(path.local_path, path.udisk_path, diff_node)
            # 修改sync_hash_udisk上相应节点中的content_hash
            sync_hash_udisk.change_content_hashcode_by_name_hashcode(
                diff_node.get_name_hashcode(), diff_node.get_content_hashcode)

        # 根据add_in_local数组， 把本地新增的文件复制到U盘 shiweihua
        for add_in_local_node in add_in_local:
            sync.move_to_udisk(path.local_path, path.udisk_path, add_in_local_node)
            # 遍历sync_hash_udisk， 如果该节点存在， 则不做任何操作,否则把新增的节点添加到sync_hash_udisk上 shiweihua
            tmp_node = sync_hash_udisk.find_by_name_hashcode(add_in_local_node.get_name_hashcode())
            if tmp_node != None:
                sync_hash_udisk.insert(tmp_node)
        # 根据sync_hash_local（delete_in_local） 数组，删除U盘上的文件,同时删除sync_hash_udisk上的相应节点（如果没有这个节点就不做任何操作） shiweihua
        for i in range(hash_algorithm.sync_hash_length):
            delete_in_local = sync_hash_local[i]
            while delete_in_local != None:
                sync.delete_from_udisk(path.local_path, delete_in_local)
                # 同时删除sync_hash_udisk上的相应节点（如果没有这个节点就不做任何操作）
                sync_hash_udisk.delete_by_name_hashcode(delete_in_local.get_name_hashcode())
                delete_in_local = delete_in_local.get_next_node()
        # 把sync_hash_udisk序列化到本地和U盘上的.synchash文件
        serialize.serialize(sync_hash_udisk, path.local_path+os.sep+".sync"+os.sep+".synchash")
        shutil.copy2(path.udisk_path + os.sep + ".sync" + os.sep + ".synchash",
                     path.local_path + os.sep + ".sync" + os.sep + ".synchash")
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
