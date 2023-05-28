from socket import *
from time import sleep

s = socket()
s.connect(('127.0.0.1',8888))

# 读取文件内容,将文件发送出去
f = open('timg.jpg','rb')

while True:
    data = f.read(1024)
    # if not data:
    #     break
    if not data:
        # 文件已经读完
        sleep(0.2) # 让上一个消息被接受完
        s.send(b'##')
        break
    s.send(data)

data = s.recv(1024)
print(data.decode())


f.close()
s.close()

