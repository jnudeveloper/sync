# coding=utf-8
# 序列化相关的代码
import os

try:
    import cPickle as pickle
except:
    import pickle


# 序列化，只需要传入路径，不用输入文件名
# 序列化成功则返回True， 不成功返回False
# author 李国雄
def serialize(hash_list, path):
    if not os.path.exists(path):
        return False
    file_stream = file(path + os.sep + ".synchash", "w")
    pickle.dump(hash_list, file_stream)
    file_stream.close()
    return True


# 反序列化，只需要传入路径，不用输入文件名
# 反序列化成功则返回该对象， 不成功返回None
# author 李国雄
def deserialize(path):
    if not os.path.exists(path):
        return None
    file_stream = file(path + os.sep + ".synchash")
    hash_list = pickle.load(file_stream)
    return hash_list
