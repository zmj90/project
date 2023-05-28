from socket import *


class UdpSocket:
    def __init__(self):
        self.u_sk = socket(AF_INET, SOCK_DGRAM)
        self.server_address = ("localhost", 2048)

    def st_rf(self):
        while True:
            try:
                word = input(">> ")
            except KeyboardInterrupt:
                return
            if not word:
                return
            self.u_sk.sendto(word.encode(), self.server_address)
            data, address = self.u_sk.recvfrom(1024)
            print(data.decode())

    def close(self):
        self.u_sk.close()


def main():
    us = UdpSocket()
    us.st_rf()
    us.close()


if __name__ == "__main__":
    main()