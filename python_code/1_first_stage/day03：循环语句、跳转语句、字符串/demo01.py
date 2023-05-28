"""
    while
"""
import random

# 死循环：循环条件永远是满足的。
while True:
    usd = int(input("请输入美元："))
    print(usd * 6.9)
    if input("输入q键退出:"):
        break  # 退出循环体

# 需求:执行三次
count = 0
while count < 3:  # 0  1  2
    count += 1
    usd = int(input("请输入美元："))
    print(usd * 6.9)
"""
    猜数字2.0:
        最多猜３次，如果猜对提示"猜对了，总共猜了?次"
        如果超过次数，提示"游戏结束".
"""
random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 3:
    # 三次以内
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break  # 退出循环体，不会执行else语句。
else:  # while的条件不满足
    # 三次以外
    print("失败")
