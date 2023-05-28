"""
udp 客户端
"""

from socket import *

# 服务端地址
server_address = ("127.0.0.1",8888)

# 创建套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 消息传输
udp_socket.sendto(b"Hello World",server_address)

data,addr = udp_socket.recvfrom(20)
print("从服务端收到:",data)


# 关闭套接字
udp_socket.close()
