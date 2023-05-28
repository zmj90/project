from socket import *


class DictClientView:
    def __init__(self, host, port=80):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.s = socket()
        self.s.connect(self.address)

    def start(self):
        while True:
            print("请输入相应的序号：<1、登录> <2、注册> <3.退出>")
            number = input(">> ")
            if number == "1":
                self.go_sign_in()
            elif number == "2":
                self.go_sign_up()
            elif number == "3":
                self.exit()

    def go_sign_in(self):
        while True:
            user = input("输入用户名：")
            self.s.send(f"U {user}".encode())
            data = self.s.recv(64)
            if not data:
                continue
            else:
                break


    def go_sign_up(self):
        pass

    def exit(self):
        pass

