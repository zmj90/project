"""
僵尸进程产生
"""

from multiprocessing import Process
from time import sleep

from signal import *
signal(SIGCHLD,SIG_IGN) #　子进程如果退出，由系统处理，父进程不处理

# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

p = Process(target=worker,args=(1,),kwargs={'name':'Tom'})
p.start()

# p.join(5)  # 回收子进程

while True:
    pass

