"""
文件读取示例
"""

f = open('file','r')

# 一次性读取文件
# data = f.read() # 读取全部文件内容
# print(type(data))
# print("读取到的数据:",data)

# 大文件循环读取文件
# while True:
#     data = f.read(1024)  # 每次读取100个字节，读到文件结尾后会返回空字符串
#     if not data:
#         break
#     print(data)

# 行读取
# data = f.readline(5)  # 最多读取5字符
# print(type(data))
# print("读取一行:",data)
# data = f.readline()
# print("读取一行:",data)

# 读取多行
# data = f.readlines()
# print(type(data))
# print("多行读取：",data)

# 迭代属性，每次获取一行
for line in f:
    print(line, end="")
    print(type(line))


f.close()