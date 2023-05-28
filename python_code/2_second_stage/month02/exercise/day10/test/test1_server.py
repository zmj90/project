# udp 套接字

from socket import *

HOST = "0.0.0.0"
PORT = 2048
ADDRESS = (HOST, PORT)

# 创建udp套接字
s = socket(2, 2)

# 绑定地址
s.bind(ADDRESS)

# 接受请求
data, address = s.recvfrom(1024)
print(data.decode())
# 回发
s.sendto(b"thanks",address)

# 关闭套接字
s.close()
