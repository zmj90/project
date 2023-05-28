from socket import *

# 1.创建套接字
tcp_socket = socket()

# 2.发起链接
server_address = ("192.168.0.103",2050)
tcp_socket.connect(server_address)

# 3.发送消息
while True:
    msg = input(">> ")
    tcp_socket.send(msg.encode())
    if not msg:
        break
    data = tcp_socket.recv(20)
    print(data.decode())

# 4.关闭套接字
tcp_socket.close()
