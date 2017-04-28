# coding=utf-8
# 内存测试的例子
# 使用方法：在本目录下执行 "python -m memory_profiler test2.py"
from memory_profiler import profile


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


# 使用方法：在本目录下执行 "python -m memory_profiler test2.py"
if __name__ == '__main__':
    my_func()
