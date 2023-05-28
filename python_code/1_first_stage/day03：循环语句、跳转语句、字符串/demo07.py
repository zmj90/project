"""
    for for
"""

# 外层循环控制行
for r in range(3):  # 0    1     2
    # 内层循环控制列　
    for c in range(4):  # 0123  0123  0123
        print("*", end=" ")
    print()

"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""
for r in range(4):
    for c in range(6):
        if c % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()

"""    外层4　　　　内层
    *              0
    **             01
    ***            012
    ****           0123
"""
for r in range(4):  # 0    1   2   3
    #
    for c in range(r + 1):  # 1   2   3   4
        print("*", end="")
    print()
