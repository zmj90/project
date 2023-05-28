from socket import *

tcp_socket = socket()
server_address = ("localhost", 2048)
tcp_socket.connect(server_address)
tcp_socket.send(b" ")
print("已发送")
tcp_socket.recv(1024)
print("已接收")
tcp_socket.close()
print("关闭")