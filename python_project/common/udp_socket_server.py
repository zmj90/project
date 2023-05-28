from socket import *


class UdpSocket:
    def __init__(self):
        self.udp_sk = socket(AF_INET, SOCK_DGRAM)  # 1.创建套接字对象
        self.udp_sk.bind(("localhost", 2048))  # 2.绑定地址

    def rf_st(self):
        """
        3、4.收发消息
        data, address = self.udp_sk.recvfrom(1024)
        result = None
        self.udp_sk.sendto(result.encode(), address)
        """
        pass

    def close(self):
        self.udp_sk.close()  # 5.关闭套接字


def main():
    udp_socket = UdpSocket()
    udp_socket.rf_st()
    udp_socket.close()
