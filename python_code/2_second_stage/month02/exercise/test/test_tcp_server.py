from socket import *

tcp_socket = socket()
tcp_socket.bind(("localhost", 2048))
tcp_socket.listen(6)
print("等待链接")
connect_socket, address = tcp_socket.accept()
data = connect_socket.recv(1024)
print(data)
n = connect_socket.send(b"")
print("已发送")
connect_socket.close()
tcp_socket.close()
