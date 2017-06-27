# coding=utf-8
# 同步相关的代码
import os
import path
import shutil
from shutil import copytree
import synchash
import serialize
import hash_algorithm


# @author shiweihua
# 根据节点信息，把本地文件移动到U盘（如果文件已经存在，则覆盖） shiweihua
def move_to_udisk(local_path, udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（local_absolute_path）
    local_absolute_path = path.change_relative_path_to_absolute_path(local_path, relative_path)
    # 把本地文件移动到U盘
    move_one_file(local_absolute_path, udisk_path, relative_path)


# @author shiweihua
# 根据节点信息，把U盘文件移动到本地(如果文件已经存在，则覆盖) shiweihua
def move_to_local(local_path, udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（udisk_absolute_path）
    udisk_absolute_path = path.change_relative_path_to_absolute_path(udisk_path, relative_path)
    # 把本地文件移动到本地
    move_one_file(udisk_absolute_path, local_path, relative_path)


# @author shiweihua
# 根据节点信息,删除U盘中的文件 shiweihua
def delete_from_udisk(udisk_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（udisk_absolute_path）
    udisk_absolute_path = path.change_relative_path_to_absolute_path(udisk_path, relative_path)
    # 如果存在这个文件，则删掉它
    if os.path.exists(udisk_absolute_path):
        os.remove(udisk_absolute_path)


# @author shiweihua
# 根据节点信息,删除本地中的文件 shiweihua
# 和delete_from_udisk差不多，可不可以合成一个？ shiweihua
# （因为这个函数是之前定义的，我怕你们会调用这个函数，所有就没有合并成一个by shiweihua）
# （不合并了，就让它这样吧 by 李国雄）
def delete_from_local(local_path, node):
    # 从node中取出相对路径relative_path
    relative_path = node.get_path()
    # 拼接相对路径得到绝对路径（local_absolute_path）
    local_absolute_path = path.change_relative_path_to_absolute_path(local_path, relative_path)
    # 如果存在这个文件，则删掉它
    if os.path.exists(local_absolute_path):
        os.remove(local_absolute_path)


# @author shiweihua
# 根据给出的路径移动文件，需要时会自动新建目录 shiweihua
def move_one_file(src, sync_path, relative_path):
    # 将relative_path按路径分隔符切割成数组relative_path_arr
    relative_path_arr = relative_path.split(os.sep)
    # 删除relative_path_arr中最后一个元素
    relative_path_arr.pop()
    # 逐步将sync_path与relative_path_arr中的元素拼接，并且检验这个目录是否存在，不存在则新建之
    tmp_sync_path = sync_path
    for tmp_folder in relative_path_arr:
        tmp_sync_path += (os.sep + tmp_folder)
        if not os.path.exists(tmp_sync_path):
            os.mkdir(tmp_sync_path)  # 目录不存在，新建之
    # 如果目的文件夹下已经存在这个文件则覆盖它，否则复制文件到目的文件夹下
    shutil.copy2(src, sync_path + os.sep + relative_path)


# @author shiweihua
# 把U盘中的全量目录pull到本地
def fully_pull(udisk_path, local_path):
    full_dir = udisk_path + os.sep + ".sync" + os.sep + ".all"
    folders = os.listdir(full_dir)
    for folder in folders:
        full_src_path = full_dir + os.sep + folder
        if os.path.isdir(full_src_path):
            copytree(full_src_path, local_path + os.sep + folder)
        elif os.path.isfile(full_src_path):
            shutil.copy2(full_src_path, local_path)
    # 在本地新建.sync目录
    os.mkdir(local_path + os.sep + ".sync")
    shutil.copy2(udisk_path + os.sep + ".sync" + os.sep + ".synchash",
                 local_path + os.sep + ".sync" + os.sep + ".synchash")
    # 将U盘.sync目录下的同步目录删除 shiweihua
    shutil.rmtree(path.udisk_path + os.sep + ".sync" + os.sep + ".all")


# @author shiweihua
# 将本地的所有文件复制到U盘的全量目录下
def fully_push(local_path, udisk_path):
    if os.path.exists(udisk_path + os.sep + ".sync" + os.sep + ".all"):
        shutil.rmtree(udisk_path + os.sep + ".sync" + os.sep + ".all")
    full_dst_dir = udisk_path + os.sep + ".sync" + os.sep + ".all"
    os.mkdir(full_dst_dir)
    folders = os.listdir(local_path)
    for folder in folders:
        if folder != ".sync":
            full_src_path = local_path + os.sep + folder
            if os.path.isdir(full_src_path):
                copytree(full_src_path, full_dst_dir + os.sep + folder)
            elif os.path.isfile(full_src_path):
                shutil.copy2(full_src_path, full_dst_dir)
    # 将本地的.synchash文件复制到U盘 shiweihua
    shutil.copy2(path.local_path + os.sep + ".sync" + os.sep + ".synchash",
                 path.udisk_path + os.sep + ".sync" + os.sep + ".synchash")


# 由于synchash.fill_sync_hash_list(sync_hash_list)还未实现，所以这个函数没有测试 shiweihua
# 已经测试 李国雄
# 本地项目初始化  见本地项目初始化流程图 shiweihua
def init_local():
    # 新建一个sync_hash数组链表 shiweihua
    sync_hash_list = synchash.FileHashList()
    # 递归扫描本地同步目录填充sync_hash数组链表 shiweihua
    sync_hash_list = synchash.fill_sync_hash_list(sync_hash_list)
    # 将sync_hash_list序列化到本地
    serialize.serialize(sync_hash_list, path.local_path + os.sep + ".sync")


# 未测试 shiweihua
# 已经测试 李国雄
# 初始化U盘
def init_udisk():
    # 在U盘上新建.sync文件夹， 在文件夹.sync中新建.synchash空文件 shiweihua
    os.mkdir(path.udisk_path + os.sep + ".sync")
    # os.mknod(path.udisk_path + os.sep + ".sync" + os.sep + ".synchash")
    # 初始化一个sync_hash空数组链表，序列化到U盘的.sync文件夹下的.synchash文件中 shiweihua
    sync_hash = synchash.FileHashList()
    serialize.serialize(sync_hash, path.udisk_path + os.sep + ".sync")


# 未测试 shiweihua
# 已经测试 李国雄
# 增量pull
def incrementally_pull():
    # 初始化diff数组 shiweihua
    diff = []
    # 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
    sync_hash_local = serialize.deserialize(path.local_path + os.sep + ".sync")
    # 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
    sync_hash_udisk = serialize.deserialize(path.udisk_path + os.sep + ".sync")
    # 遍历比较sync_hash_local和sync_hash_udisk，得到数组diff、sync_hash_udisk、sync_hash_local 看增量pull流程图 shiweihua
    for i in range(hash_algorithm.sync_hash_length):
        local_node = sync_hash_local.hash_list[i]
        while local_node is not None:
            temp_flag = 0
            udisk_node = sync_hash_udisk.hash_list[i]
            while udisk_node is not None:
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
        move_to_local(path.local_path, path.udisk_path, diff_node)
        delete_from_udisk(path.udisk_path, diff_node)
    # 根据现在的sync_hash_udisk， 把U盘新增的文件复制到本地， 同时把U盘上的该文件删除 shiweihua
    for i in range(hash_algorithm.sync_hash_length):
        add_in_other = sync_hash_udisk.hash_list[i]
        while add_in_other is not None:
            move_to_local(path.local_path, path.udisk_path, add_in_other)
            delete_from_udisk(path.udisk_path, add_in_other)
            add_in_other = add_in_other.get_next_node()
    # 根据现在的sync_hash_local， 在本地上删除U盘没有的文件 shiweihua
    for i in range(hash_algorithm.sync_hash_length):
        # sync_hash_udisk应该是sync_hash_local？ shiweihua(已修改by shiweihua 如果没问题就将TODO去掉)（已去 by 李国雄）
        delete_in_other = sync_hash_local.hash_list[i]
        while delete_in_other is not None:
            delete_from_local(path.local_path, delete_in_other)
            delete_in_other = delete_in_other.get_next_node()
    # 把U盘的.synchash文件复制到本地 shiweihua
    shutil.copy2(path.udisk_path + os.sep + ".sync" + os.sep + ".synchash",
                 path.local_path + os.sep + ".sync" + os.sep + ".synchash")


# TODO 未测试 shiweihua
# 增量pull
def incrementally_push():
    # 初始化数组： add_in_local、 diff shiweihua
    add_in_local = []
    diff = []
    # 反序列化本地的.synchash文件得到哈希数组链表sync_hash_local shiweihua
    sync_hash_local = serialize.deserialize(path.local_path + os.sep + ".sync")
    # 反序列化U盘的.synchash文件得到哈希数组链表sync_hash_udisk shiweihua
    sync_hash_udisk = serialize.deserialize(path.udisk_path + os.sep + ".sync")
    # 递归扫描本地目录，得到一个包含本地同步目录下所有文件路径的数组（.sync目录除外） shiweihua
    file_path_arr = path.get_all_file_path(path.local_path)
    # 根据file_path_arr数组计算diff、sync_hash_udisk、sync_hash_local 看增量push流程图 shiweihua
    for filename in file_path_arr:
        # 将绝对路径变成相对路径relative_path
        relative_path = path.change_absolute_path_to_relative_path(path.local_path, filename)
        # 计算文件名hash
        name_hashcode = hash_algorithm.get_name_hashcode(relative_path)
        node_in_udisk = sync_hash_udisk.find_by_name_hashcode(name_hashcode)
        if node_in_udisk is not None:  # 判断节点是否在sync_hash_udisk中
            # 如果在sync_hash_udisk中，计算文件内容hash
            # 这里应该传绝对路径吧 shiweihua (已修改 by shiweihua， 如果没问题就把TODO去掉)（已去 by 李国雄）
            content_hashcode = hash_algorithm.get_content_hashcode(filename)
            if content_hashcode != node_in_udisk.get_content_hashcode():
                # 把该文件节点放到diff数组中
                node = synchash.FileHashNode(path.local_path, relative_path)
                diff.append(node)
        node_in_local = sync_hash_local.find_by_name_hashcode(name_hashcode)
        if node_in_local is not None:  # 判断节点是否在sync_hash_local中
            # 如果在sync_hash_local中则从sync_hash_local中删除这个节点
            sync_hash_local.delete_by_name_hashcode(name_hashcode)
        else:
            # 如果不在sync_hash_local中则把扫描的文件节点放到add_in_local中
            node = synchash.FileHashNode(path.local_path, relative_path)
            add_in_local.append(node)
    # 根据diff数组,把本地对应的文件覆盖U盘的文件,同时修改sync_hash_udisk上相应节点中的content_hash shiweihua
    for diff_node in diff:
        # 为什么是移动到本地？ 写错了？ shiweihua(已修改 by shiweihua 如果没问题就把TODO去掉)（已去 by 李国雄）
        move_to_udisk(path.local_path, path.udisk_path, diff_node)
        # 修改sync_hash_udisk上相应节点中的content_hash
        sync_hash_udisk.change_content_hashcode_by_name_hashcode(
            diff_node.get_name_hashcode(), diff_node.get_content_hashcode())

    # 根据add_in_local数组， 把本地新增的文件复制到U盘 shiweihua
    for add_in_local_node in add_in_local:
        move_to_udisk(path.local_path, path.udisk_path, add_in_local_node)
        # 遍历sync_hash_udisk， 如果该节点存在， 则不做任何操作,否则把新增的节点添加到sync_hash_udisk上 shiweihua
        tmp_node = sync_hash_udisk.find_by_name_hashcode(add_in_local_node.get_name_hashcode())
        if tmp_node is None:
            sync_hash_udisk.insert(add_in_local_node)
    # 根据sync_hash_local（delete_in_local） 数组，删除U盘上的文件,同时删除sync_hash_udisk上的相应节点（如果没有这个节点就不做任何操作） shiweihua
    for i in range(hash_algorithm.sync_hash_length):
        delete_in_local = sync_hash_local.hash_list[i]
        while delete_in_local is not None:
            delete_from_udisk(path.local_path, delete_in_local)
            # 同时删除sync_hash_udisk上的相应节点（如果没有这个节点就不做任何操作）
            sync_hash_udisk.delete_by_name_hashcode(delete_in_local.get_name_hashcode())
            delete_in_local = delete_in_local.get_next_node()
    # 把sync_hash_udisk序列化到本地和U盘上的.synchash文件
    serialize.serialize(sync_hash_udisk, path.local_path + os.sep + ".sync")
    shutil.copy2(path.local_path + os.sep + ".sync" + os.sep + ".synchash",
                 path.udisk_path + os.sep + ".sync" + os.sep + ".synchash")
