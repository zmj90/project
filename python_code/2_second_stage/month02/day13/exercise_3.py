"""
练习:
拷贝一个文件夹(只考虑其中的普通文件), 文件夹中的每个文件的拷贝看做是一个独立的进程事件,
使用进程池来完成这个工作

练习: 在上一个练习的基础上完成
拷贝文件夹过程中,实时的显示拷贝进度百分比

文件夹大小 = 所有文件大小之和
"""

from  multiprocessing import Pool,Queue
import os

old_folder = "/home/tarena/File/"
new_folder = "/home/tarena/File-备份/"
os.mkdir(new_folder) # 创建新文件夹

q = Queue()  # 消息队列

# 获取文件夹大小
def total_size():
    size = 0
    file_list = os.listdir(old_folder)
    for file in file_list:
        size += os.path.getsize(old_folder+file)
    return size

# 复制每一个文件 (进程池要执行的内容)
def copy_file(file):
    fr = open(old_folder+file,'rb')
    fw = open(new_folder+file,'wb')
    # 拷贝一个文件
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)  # 向目标写入内容
        q.put(n) # 已经写入的字节数放入到消息队列中
    fr.close()
    fw.close()

def main():
    pool = Pool(4)
    file_list = os.listdir(old_folder) # 文件列表
    # 放入事件
    for file in file_list:
        pool.apply_async(copy_file,args=(file,))

    pool.close()

    all_size = total_size() # 总大小
    copy_size = 0
    while copy_size < all_size:
        copy_size += q.get()
        print("已拷贝 : %.2f%%"%(copy_size/all_size*100))



    pool.join()

main()







