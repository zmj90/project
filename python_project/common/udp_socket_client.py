from socket import *


class UdpSocket:
    def __init__(self):
        self.udp_sk = socket(AF_INET, SOCK_DGRAM)  # 1.创建套接字对象
        self.server_address = ("localhost", 2048)  # 2.确定服务端地址

    def st_rf(self, data):
        """
        # 3、4.发收消息
        self.udp_sk.sendto(data, self.server_address)
        result, address = self.udp_sk.recvfrom(1024)
        return result, address
        """
        pass

    def close(self):
        self.udp_sk.close()  # 5.关闭套接字


def main():
    udp_socket = UdpSocket()
    udp_socket.st_rf("hello world".encode())
    udp_socket.close()
