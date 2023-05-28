from socket import *


class TcpSocket:
    def __init__(self):
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.server_address = ("localhost", 2048)

    def socket_(self):
        self.tcp_socket.connect(self.server_address)
        while True:
            msg = input(">> ")
            self.tcp_socket.send(msg.encode())
            if msg == '##':
                break
            data = self.tcp_socket.recv(1024)
            print(data.decode())
        self.tcp_socket.close()
