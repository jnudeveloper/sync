[sync]
sync 是一个同步工具，它使用U盘作为中间媒介，实现多个设备之间的数据同步。

[操作系统]
windows
理论上Python跨平台，写的代码可以在linux/unix上执行，但是没有测试过

[IDE]
名称：PyCharm
下载地址：https://www.jetbrains.com/pycharm/
社区版免费，用社区版就可以了

[目录结构]
sync/src  源程序代码、cpu时间测试和内存测试的代码
sync/test  单元测试代码、运行时间测试代码

[安装与运行]
1.安装Python 2.7x运行环境
    Python下载地址：https://www.python.org/downloads/
2.添加Python库：wxPython(图形界面)、line_profiler(cpu时间测试)、memory_profiler(内存测试)
    pip install wxPython
    pip install line_profiler
    pip install memory_profiler
3.运行main.py文件（命令行界面）、运行main_win.py文件（图形界面）
4.运行各个测试脚本可以进行相应的测试
