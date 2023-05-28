"""
    选择语句：运行时,根据某些条件决定是否执行语句
"""

sex = input("请输入性别：")
if sex == "男":
    print("您好，先生！")
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")


# 真值表达式
if "a":
    # if bool("a"):
    print("真值")

str_input = input("请输入：")
if str_input:
    print("输入的字符串不是空的")


# 条件表达式:有选择性的为变量进行赋值
# sex = None
# if input("请输入性别:") == "男":
#     sex = 1
# else:
#     sex = 0
# print(sex)
sex = 1 if input("请输入性别:") == "男" else 0
print(sex)

sex = 1 if input("请输入性别:") == "男" else None
print(sex)

year = int(input("请输入年份："))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
