"""
编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端

           服务端     接收内容 --> 写入到一个文件中

           客户端     读取图片内容  --> 发送给服务端
"""
from socket import *
from time import *

# 设置监听套接字
s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(3)

#  接收数据 --> 写入文件
c, addr = s.accept()
print("Connect from", addr)

f = open("zly.jpg", 'wb')  # 写如的文件

# 循环接收内容,写入文件
start = time()
while True:
    data = c.recv(1024)
    if data[-1:-3:-1] == b"##":
        f.write(data[:-2])
        break
    f.write(data)
end = time() - start
print(end)
f.close()
c.close()
s.close()
