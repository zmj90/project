from threading import Thread, Event, Lock
from time import sleep
e1 = Event()
e2 = Event()
lock = Lock()

def fun01():
    for i in range(1,53,2):
        e2.set()
        e2.wait()
        # lock.acquire()
        for j in range(i,i+2):
            print(j,sep="",end="")
        # lock.release()
        e1.set()
        e2.wait()

def fun02():
    for i in range(65,91):
        e1.wait()
        # lock.acquire()
        print(chr(i))
        # lock.release()
        e2.set()
        e1.clear()


t1 = Thread(target=fun01)
t2 = Thread(target=fun02)



t1.start()
t2.start()

t1.join()
t2.join()
# print(chr(65))