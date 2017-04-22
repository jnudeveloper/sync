# coding=utf-8
# 运行时间测试的例子
import cProfile


# 待测试的例子方法
def sum_num( max_num):
    total = 0
    for i in range(max_num):
        total += i
    return total


def get_sum_num():
    total = 0
    for i in range(40000):
        total += i
    t1 = sum_num(100000)
    t2 = sum_num(400000)
    return total


cProfile.run("get_sum_num()")
