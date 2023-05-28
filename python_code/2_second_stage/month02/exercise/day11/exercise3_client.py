from socket import *


class InputMessage:
    def __init__(self):
        self.list_row = []
        self.column = ("姓名","年龄","性别","分数")

    def get_element(self):
        for i in self.column:
            value = input("请输入%s:" % i)
            if not value:
                return
            self.list_row.append(value)
        return "-".join(self.list_row)


class Socket:
    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.server_address = ('127.0.0.1', 2048)
        self.target = InputMessage()

    def sendto_receive(self):
        while True:
            data = self.target.get_element()
            if not data:
                return
            self.udp_socket.sendto(data.encode(),self.server_address)
            data,address = self.udp_socket.recvfrom(30)
            print(data.decode())

    def close(self):
        self.udp_socket.close()


def main():
    sk = Socket()
    sk.sendto_receive()
    sk.close()
    print("客户端关闭了。")


if __name__ == "__main__":
    main()