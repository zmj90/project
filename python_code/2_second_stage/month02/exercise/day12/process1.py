import multiprocessing as mp
from time import sleep

a = 1

def fun():
    # print("开始一个进程")
    for i in range(2):
        # sleep(1)
        print("我是子进程")
        # print(a,b)


p = mp.Process(target=fun,name=123)

p.start()
print(a)
print(p.__dict__)
print(p.name)
id1 = p.pid
for i in range(2):
    # sleep(1)
    print("我是父进程")
p.join()
