"""
socket 模块使用
"""
import  socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(udp_socket)
print('hello world')

# 关闭套接字
udp_socket.close()
