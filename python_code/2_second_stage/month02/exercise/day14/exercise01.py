"""
练习:
线程: 模拟会场出票系统 , 现有有 500张票 记为 (T1 .... T500)
由于票的顺序涉及到座位排布,所以票必须按照顺序卖出,有10个窗口(w1--w10)同时买票
每张票出票时间为 0.1秒.
按照上述描述使用多线程完成,每个线程代表一个窗口,将票卖出,直到所有票卖完
卖出时打印下哪个窗口卖了哪张
w1 --- T48
"""
from threading import Thread
from time import sleep

list01 = []
for i in range(100,0,-1):
    list01.append(f"T{i}")


def ticket(number):
    while list01:
        sleep(0.1)
        if not list01:
            break
        t = list01.pop()
        print(f"{number}----{t}")


list02 = []
for i in range(1,11):
    t = Thread(target=ticket,args=(f"M{i}",))
    list02.append(t)
    t.start()
[i.join() for i in list02]
