"""
udp 服务端
"""

from socket import *

# 创建套接字
# udp_socket = socket(AF_INET,SOCK_DGRAM)
udp_socket = socket(2, 2)

# 绑定地址
udp_socket.bind(("127.0.0.1",8888))

# 消息传输
print("等待接收一个消息.....")
data,addr = udp_socket.recvfrom(20)
print("接收到",addr,":",data)

# 给客户端回发
udp_socket.sendto(b"Thanks",addr)


# 关闭套接字
udp_socket.close()
