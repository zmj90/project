"""
练习:
拷贝一个文件夹(只考虑其中的普通文件), 文件夹中的每个文件的拷贝看做是一个独立的进程事件,
使用进程池来完成这个工作
练习: 在上一个练习的基础上完成
拷贝文件夹过程中,实时的显示拷贝进度百分比
文件夹大小 = 所有文件大小之和
"""
from multiprocessing import Pool, Queue
import os

# 创建消息队列对象
q = Queue()

# 创建目录
os.mkdir("copy")


def get_size(path):
    n = 0
    for item in os.listdir(path):
        n += os.path.getsize("day13/" + item)
    return n


# 复制单个文件
def copy(file):
    f1 = open("day13/" + file, "rb")
    f2 = open("copy/" + file, "wb")
    while True:
        data = f1.read(1024)
        if not data:
            break
        n = f2.write(data)
        q.put(n)
    f1.close()
    f2.close()


# 创建进程池
pool = Pool(4)

# 将事件加入进程池队列执行
list_file = os.listdir("day13")
for item in list_file:
    pool.apply_async(copy, (item,))

# 关闭进程池 ,不能再加入新的事件
pool.close()

n = 0
while n < get_size("day13"):
    n += q.get()
    print("复制了%.2f%%" % (n / get_size("day13") * 100))
# 阻塞等待回收进程池
pool.join()
