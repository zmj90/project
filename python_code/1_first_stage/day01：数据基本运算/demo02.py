"""
    核心数据类型
"""
# 1. None
a01 = "苏大强"
# 解除变量与数据的绑定关系
a01 = None
# 使用None占位
sex = None

# 2. 整形int
# 十进制
num01 = 20
# 二进制
print(0b10)  # 2
# 八进制
print(0o10)  # 8
# 十六进制
print(0x10)  # 16

# 3.　浮点数float
print(1.5)
# 科学计数法:表示过小或过大的值很明确
# 1.23e-25
print(0.000000000000000000000000123)

# 4. 字符串str
print("1.5")
a = 10
print(a)  # 打印变量　　10
print("a")  # 打印字符串 a

int(1.9)


# 混合类型自动升级：
# 1 + 2.14  返回的结果是 3.14
# 1 + 3.0  返回结果是:  4.0
# str -> int
data01 = int("3")
# int -> str
data02 = str(5)

# str -> float
data03 = float("1.2")
# float -> str
data04 = str(1.2)

# int -> float
data05 = float(250)
# float -> int
data06 = int(1.9)
print(data06)  # 1 向下取整(截断删除)

# 注意：字符串转换为其他类型时,
# 必须是目标类型的字符串表达形式
# print(int("10.5"))　# 报错
# print(float("abc"))# 报错
