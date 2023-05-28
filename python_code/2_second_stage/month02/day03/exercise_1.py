#!/usr/bin/python3

"""
 编写一个程序，运行程序可以打印当前的时间（time）,然后打印一个双色球号码
         要求在终端能直接 ./ssq.py 运行

         random模块 --》 randint() 生成随机正数

         红 1--33
         蓝 1--16
"""

from time import ctime
from random import randint

l = []  # 存储最后生成的号码

# 生成6个红球
while len(l) < 6:
    num = randint(1,33) # 生成一个红球
    # 红球6个不能重复
    if num not in l:
        l.append(num)

l.sort() # 排序
l.append(randint(1,16)) # 添加一个蓝球

print(ctime(),":",l)
print(type(ctime()))
