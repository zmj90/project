"""
进程属性演示
"""

from multiprocessing import Process
import time

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

# 创建进程对象
p = Process(target = fun)

# 这个子进程会随父进程的退出而退出
p.daemon = True

p.start()

p.name = "print_time"
print("进程名称:",p.name)
print("进程PID:",p.pid)
print("是否在声明周期:",p.is_alive())


# p.join(2)
# print("======================================")