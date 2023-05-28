from socket import *

# 全局变量
HOST = "0.0.0.0"
PORT = 2048
ADDRESS = (HOST, PORT)

# 启动窗口
def main():
    tcp_socket = socket()
    tcp_socket.bind(ADDRESS)
    tcp_socket.listen(3)

    while True:
        connect,address = tcp_socket.accept()
