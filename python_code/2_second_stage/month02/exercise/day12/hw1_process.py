# 1. 将一个文件拆分为两个小文件,按照字节数平均拆分, 使用父进程和子进程同时进行
# 一个进程获取半部分,换一个进程获取下半部分(一点点拿，一点点算，提高效率)

from multiprocessing import Process
import os

# 确定文件中间值
file = open("背影.txt", "rb")
print(id(file))
file_size = os.path.getsize("背影.txt")
if file_size % 2 == 0:
    n = file_size / 2
else:
    n = file_size // 2 + 1


# 写入文件1
def write1(n1):

    file = open("背影.txt", "rb")
    print(id(file))
    file1 = open("1.txt", "wb")
    data = file.read(n1)
    file1.write(data)
    file1.close()


# 写入文件2
def write2(n2):
    file2 = open("2.txt", "wb")
    file.seek(n2 + 1, 0)
    data = file.read()
    file2.write(data)
    file2.close()


# 创建进程对象
p = Process(target=write1, args=(n,))

# 启动进程
p.start()

write2(n)

p.join()

file.close()
