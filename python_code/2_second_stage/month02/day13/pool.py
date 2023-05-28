"""
进程池演示

* 父进程退出,进程池会随之销毁
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池函数 (在进程池创建之前声明)
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

# 创建进程池
pool = Pool(4)

# 向进程池等待队列中加入事件
for i in range(10):
    msg = "Tedu%d"%i
    pool.apply_async(worker, (msg,))  # 进程池已经可以执行事件


# 关闭进程池 ,不能再加入新的事件
pool.close()

# 阻塞等待回收进程池
pool.join()