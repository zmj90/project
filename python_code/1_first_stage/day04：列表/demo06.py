"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = []
for r in list01:
    for c in list02:
        list03.append(r + c)

print(list03)

list04 = [r + c for r in list01 for c in list02]
print(list04)

# 练习:列表的全排列
# [“香蕉”,"苹果","哈密瓜"]
# [“可乐”,"牛奶"]
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["可乐", "牛奶"]
list03 = []
for r in list01:
    for c in list02:
        list03.append(r + c)
list04 = [r + c for r in list01 for c in list02]
print(list03)
print(list04)

combs = []
for x in [1, 2, "3"]:
    if isinstance(x, int):
        for y in [3, 1, 4]:
            combs.append((x, y))
print(combs)
l1 = [(x, y) for x in [1, 2, "3"] if isinstance(x, int) for y in [3, 1, 4]]
print(l1)
