本文件夹（src)主要是系统源代码，同时还有cpu时间测试和内存测试的代码
因为这两个的测试的代码改到test目录出现一些问题，还无法解决，所以放在了这个目录

各个文件（模块）的功能：
cpu_time0.py  cpu_time1.py  cpu_time2.py  测试cpu时间，3个脚本的数据显示方式不一样
gui.py  图形界面控件设计
hash_algorithm.py  计算hash值
main.py  命令行界面的主函数、主流程
main_win.py  图形界面的主函数、主流程
memory.py  测试内存
path.py  命令行界面的路径（目录）操作
path_win.py  图形界面的路径（目录）操作
process.py  命令行界面的具体流程
process_win.py  图形界面的具体流程
prompt.py  提示语汇总（有些提示语没有写在这里，直接写在其他文件了，先不管这么多了）
serialize.py  序列化与反序列化
sync.py  同步算法实现
synchash.py  hash数组链表（记录文件信息的数据机构）
