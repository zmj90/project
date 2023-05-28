from socket import *

server_addr = ("192.168.94.140",8888)

# 创建tcp套接字  默认参数就是创建tcp套接字
tcp_socket = socket()

# 发起链接
tcp_socket.connect(server_addr)

# 发送接收消息
while True:
    msg = input(">>") # 输入##退出
    tcp_socket.send(msg.encode())
    if msg == '##':
        break
    data = tcp_socket.recv(1024)
    print("在线mm:",data.decode())


tcp_socket.close()


