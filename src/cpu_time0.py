# coding=utf-8
# 性能测试：测试程序运行时占用的cpu时间
# 使用方法：在本目录下执行 "kernprof -l -v cpu_time0.py"

import os
import shutil
import path
import sync


def tmp1():
    test_local_path = path.test_local_path_root + os.path.sep + path.test_relative_path
    test_udisk_path = path.test_udisk_path_root + os.path.sep + path.test_relative_path
    test_remote_path = path.test_remote_path_root + os.path.sep + path.test_relative_path
    if os.path.exists(test_local_path + os.path.sep + ".sync"):
        shutil.rmtree(test_local_path + os.path.sep + ".sync")
    if os.path.exists(test_local_path + os.path.sep + "test"):
        shutil.rmtree(test_local_path + os.path.sep + "test")
    if os.path.exists(test_udisk_path):
        shutil.rmtree(test_udisk_path)
    if os.path.exists(test_remote_path):
        shutil.rmtree(test_remote_path)
    os.mkdir(test_udisk_path)
    os.mkdir(test_remote_path)

    # 1.本地新增测试需要的文件夹、文件
    os.mkdir(test_local_path + os.path.sep + "test")
    os.mkdir(test_local_path + os.path.sep + "test" + os.path.sep + "test2")
    os.mkdir(test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3")
    file_temp = file(test_local_path + os.path.sep + "test" + os.path.sep + "update_local_test_1.txt", "w")
    file_temp.write("update_local_test_1.txt")
    file_temp.close()
    file_temp = file(test_local_path + os.path.sep + "test" + os.path.sep + "delete_local_test_1.txt", "w")
    file_temp.write("delete_local_test_1.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "update_local_test_2.txt", "w")
    file_temp.write("update_local_test_2.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "delete_local_test_2.txt", "w")
    file_temp.write("delete_local_test_2.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "update_local_test_3.txt",
        "w")
    file_temp.write("update_local_test_3.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "delete_local_test_3.txt",
        "w")
    file_temp.write("delete_local_test_3.txt")
    file_temp.close()
    path.local_path = test_local_path
    path.udisk_path = test_udisk_path


def tmp2():
    test_local_path = path.test_local_path_root + os.path.sep + path.test_relative_path
    test_udisk_path = path.test_udisk_path_root + os.path.sep + path.test_relative_path
    test_remote_path = path.test_remote_path_root + os.path.sep + path.test_relative_path
    file_temp = file(test_local_path + os.path.sep + "test" + os.path.sep + "add_local_test_1.txt", "w")
    file_temp.write("add_local_test_1.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "add_local_test_2.txt", "w")
    file_temp.write("add_local_test_2.txt")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "add_local_test_3.txt",
        "w")
    file_temp.write("add_local_test_3.txt")
    file_temp.close()
    # 5.本地修改文件
    file_temp = file(test_local_path + os.path.sep + "test" + os.path.sep + "update_local_test_1.txt", "w")
    file_temp.write("update_local_test_1.txt local_update")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "update_local_test_2.txt", "w")
    file_temp.write("update_local_test_2.txt local_update")
    file_temp.close()
    file_temp = file(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "update_local_test_3.txt",
        "w")
    file_temp.write("update_local_test_3.txt local_update")
    file_temp.close()
    # 6.本地删除文件
    os.remove(test_local_path + os.path.sep + "test" + os.path.sep + "delete_local_test_1.txt")
    os.remove(test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "delete_local_test_2.txt")
    os.remove(
        test_local_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "delete_local_test_3.txt")
    # 7.远程新增文件
    file_temp = file(test_remote_path + os.path.sep + "test" + os.path.sep + "add_remote_test_1.txt", "w")
    file_temp.write("add_remote_test_1.txt")
    file_temp.close()
    file_temp = file(
        test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "add_remote_test_2.txt", "w")
    file_temp.write("add_remote_test_2.txt")
    file_temp.close()
    file_temp = file(
        test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "add_remote_test_3.txt",
        "w")
    file_temp.write("add_remote_test_3.txt")
    file_temp.close()
    # 8.远程修改文件
    file_temp = file(test_remote_path + os.path.sep + "test" + os.path.sep + "update_local_test_1.txt", "w")
    file_temp.write("update_local_test_1.txt remote_update")
    file_temp.close()
    file_temp = file(
        test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "update_local_test_2.txt", "w")
    file_temp.write("update_local_test_2.txt remote_update")
    file_temp.close()
    file_temp = file(
        test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "update_local_test_3.txt",
        "w")
    file_temp.write("update_local_test_3.txt remote_update")
    file_temp.close()
    # 9.远程删除文件
    os.remove(test_remote_path + os.path.sep + "test" + os.path.sep + "delete_local_test_1.txt")
    os.remove(test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "delete_local_test_2.txt")
    os.remove(
        test_remote_path + os.path.sep + "test" + os.path.sep + "test2" + os.path.sep + "test3" + os.path.sep + "delete_local_test_3.txt")


@profile
def test_cpu_time():
    test_local_path = path.test_local_path_root + os.path.sep + path.test_relative_path
    test_udisk_path = path.test_udisk_path_root + os.path.sep + path.test_relative_path
    test_remote_path = path.test_remote_path_root + os.path.sep + path.test_relative_path
    tmp1()
    # 2.初始化
    sync.init_local()
    sync.init_udisk()
    # 3.1.全量push
    sync.fully_push(path.local_path, path.udisk_path)
    # 3.2.全量pull
    path.local_path = test_remote_path
    sync.fully_pull(path.udisk_path, path.local_path)
    # 4.本地新增文件
    tmp2()

    # 10.本地增量push、远程增量pull
    path.local_path = test_local_path
    path.udisk_path = test_udisk_path
    sync.incrementally_push()
    path.local_path = test_remote_path
    sync.incrementally_pull()


if __name__ == "__main__":
    test_cpu_time()







