"""
字节串类型
注意： 所有的字符串，都能转换为字节串
      但并不是所有字节串都能转换为字符串
"""

# s = "Hello world"
# print(type(s))
# print(s)

# 定义一个字节串（英文字符表达方式）
# s = b"Hello world"  # 表示在内存中存储一个二进制数据 这个二进制数据是 Hello world
# print(type(s))
# print(s)

# # 定义中文或者变量字节串
a = "你好"
s = a.encode()  # 将字符串转换为字节串
# print(type(s))
# print(s)
#
# 字节串 转换为字符串
print("=============================")
print(s.decode()) # 将字节串转换为字符串