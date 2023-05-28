"""
编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端

           服务端     接收内容 --> 写入到一个文件中

           客户端     读取图片内容  --> 发送给服务端
"""
from socket import *

# 设置监听套接字
s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)


#  接收数据 --> 写入文件
c,addr = s.accept()
print("Connect from",addr)

f = open("zly.jpg",'wb') # 写如的文件

# 循环接收内容,写入文件
while True:
    data = c.recv(1024)
    # if not data:
    #     break
    if data == b"##":
        break
    f.write(data)


c.send("文件上传成功".encode())


f.close()
c.close()
s.close()














