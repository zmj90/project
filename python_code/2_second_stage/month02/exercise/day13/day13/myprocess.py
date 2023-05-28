"""
自定义进程类
"""
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,val1,val2):
        super().__init__()  #　还行父类的ｉｎｉｔ方法
        self.val1 = val1
        self.val2 = val2

    def fun1(self):
        print(self.val1 + self.val2)

    def fun2(self):
        print(self.val1 - self.val2)
    
    # 关键方法
    def run(self):
        print("运行ｒｕｎ.....")
        self.fun1()
        self.fun2()


p = MyProcess(1,2)
p.start() #　自动执行ｒｕｎ方法，将ｒｕｎ方法作为一个进程内容来执行
p.join()


