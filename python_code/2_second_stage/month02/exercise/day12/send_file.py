from socket import *

s = socket()
s.connect(('127.0.0.1',8888))

# 读取文件内容,将文件发送出去
f = open('timg.jpg','rb')

while True:
    data = f.read(1024)
    if not data:
        # 文件已经读完
        s.send(b'##')
        break
    s.send(data)

f.close()
s.close()

