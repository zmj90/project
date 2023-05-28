"""
    列表推导式
"""

# 将list01中所有元素,增加１以后存入list02中.
list01 = [5, 56, 6, 7, 7, 8, 19]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
list02 = [item + 1 for item in list01]
print(list02)
# 将list01中大于１０元素,增加１以后存入list02中.
# list02 = []
# for item in list01:
#     if item >10:
#         list02.append(item + 1)
list02 = [item + 1 for item in list01 if item > 10]
