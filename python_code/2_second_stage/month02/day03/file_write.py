"""
写文件示例
"""

# f = open('file','w')
f = open('file','a')  # 追加
# f = open('file','wb')


# 写入内容
# n = f.write("感恩白衣死战，龙魂不死\n".encode()) # 二进制方式要写字节穿
# print("写入了%d个字节"%n)
#
# f.write("哈哈啊\n".encode())


# 写入列表内容
l = ["哈喽，死鬼\n","哎呀，干啥\n"]
re = f.writelines(l)


print(type(re))
print(type(None))
print(None)

f.close()