"""
消息队列演示
"""

from multiprocessing import Process, Queue

# 创建消息队列 (父进程中创建)
q = Queue()


def request():
    name = "Levi"
    passwd = "123"
    q.put(name)
    q.put(passwd)


def handle():
    name = q.get()
    passwd = q.get()
    print("获取用户名:",name)
    print("获取密码:",passwd)

p1 = Process(target = request)
p2 = Process(target= handle)
p1.start()
p2.start()
p1.join()
p2.join()
