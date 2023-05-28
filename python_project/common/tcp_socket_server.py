from socket import *


class TcpSocket:
    def __init__(self):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.bind(("localhost", 2048))
        self.tcp_socket.listen(6)

    def socket_(self):
        connect_socket, address = self.tcp_socket.accept()
        while True:
            data = connect_socket.recv(1024)
            if data.decode() == '##':
                break
            print(data.decode())
            connect_socket.send("hello world".encode())
        connect_socket.close()
        self.tcp_socket.close()
