"""
练习：　
求100000以内的质数之和,计算所用时间

分别使用单个进程求解

4个进程同时执行求解    分为4份  1--25000  250001-50000...

10个进程同时执行求解   分为10份  1--10000  10001-20000...
"""
from time import time
from multiprocessing import Process

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time()
        res = f(*args,**kwargs)
        end_time = time()
        print("函数执行时间:",end_time - start_time)
        return res
    return  wrapper

# 判断一个数是否为质数
def is_prime(n):
    if n < 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# 单个进程求和
@timeit
def no_process():
    prime = []
    # 逐个判断
    for i in range(100000):
        if is_prime(i):
            prime.append(i)
    print(sum(prime))


class Prime(Process):
    def __init__(self,begin,end):
        super().__init__()
        self.begin = begin # 开始数字
        self.end = end # 结束数字

    # 求 begin --- end 区间内质数之和
    def run(self):
        prime = []
        # 逐个判断
        for i in range(self.begin,self.end):
            if is_prime(i):
                prime.append(i)
        print(sum(prime))


@timeit
def process_4():
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(i,i+25000)  # 创建4个进程
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

@timeit
def process_10():
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)  # 创建10个进程
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

# 单个进程执行时间: 30.28606939315796
# no_process()
# 454396538
# 函数执行时间: 56.06134819984436

# 4个进程 函数执行时间: 20.90862011909485
# process_4()

# 10进程 函数执行时间: 18.958105325698853
# process_10()






