"""
    求100000以内的质数之和,计算所用时间
"""
import time
from multiprocessing import Process


def function_execute_time(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrap


def is_prime(value):
        if value == 2:
            return True
        for i in range(2,value):
            if value % i == 0:
                return False
        return True


class MyProcess(Process):
    def __init__(self, val1, val2):
        super().__init__()  # 还行父类的ｉｎｉｔ方法
        self.val1 = val1
        self.val2 = val2

    # 关键方法
    def run(self):
        n = 0
        for i in range(self.val1, self.val2):
            if is_prime(i):
                n += i
        print(n)


@function_execute_time
def process_1():
    n = 0
    for i in range(1, 100000):
        if is_prime(i):
            n += i
    print(n)


@function_execute_time
def process_4():
    jobs = []
    for i in range(1, 100000, 25000):
        p = MyProcess(i, i + 25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]


@function_execute_time
def process_10():
    jobs = []
    for i in range(1, 100000, 10000):
        p = MyProcess(i, i + 10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]


process_1()
# process_4()
# process_10()
