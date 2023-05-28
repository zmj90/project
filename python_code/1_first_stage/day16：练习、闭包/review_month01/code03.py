"""
    课程三:
        1. Python 程序结构
            包：文件夹
                __init__.py
            模块：文件
            导入成功的唯一标准：
                导入路径 + sys.path  --> 真实路径
        2. 异常：
            现象：程序不在向下执行,而是不断向上返回.
            目的：将异常状态转换为正常状态
                 保障程序可以按照既定的流程执行
        3. 迭代：
            for 循环原理：__iter__      __next__      try
                      返回迭代器    获取下一个元素    raise
            可迭代对象iterable：__iter__,可以参与for
            迭代器iterator：__next__,可以用一种方式获取数据
        4. 生成器
            原理：可迭代对象  +  迭代器
            优势：惰性(延迟)操作 --> 节省内存
                 循环一次  计算一次 返回一个
        5. 函数式编程
            面向过程编程：用函数隐藏细节,突显步骤.
            面向对象编程：找人?干么?
            函数式编程：将函数作为参数(传递核心逻辑)
                      将函数作为返回值(逻辑连续)
                           装饰器外层函数负责拦截调用
                                内层函数负责包裹新功能与旧功能
"""
# 1.
# 导入包中的模块：包中有没有__init__.py都可以
# from p1.m1 import func01
#
# func01()

# 导入包：自动执行__init__模块.py
# 必须在p1的__init__.py中__all__ = ["m1"]
from p1 import *

m1.func01()


# 必须在p1的__init__.py中import p1.m1
# import p1
# p1.m1.func01()

# 创建对象自动执行__init__函数
class Wife:
    def __init__(self):
        pass


# 3.
list01 = [4, 54, 65, 67, 7]
# 快捷键：iter + 回车
for item in list01:
    print(item)
# 快捷键：itere + 回车
for i, item in enumerate(list01):
    print(i, item)
