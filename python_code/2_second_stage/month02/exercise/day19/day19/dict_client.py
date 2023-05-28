"""
dict 客户端

* 发起请求
* 获取结果为用户展示
"""

from socket import *
import sys


class DictClientView:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.s = socket()
        self.s.connect(self.address)

    def main(self):
        while True:
            print("请输入相应的序号：<1、登录> <2、注册> <3.退出>")
            cmd = input(">> ")
            if cmd == "1":
                self.do_sign_in()
            elif cmd == "2":
                self.do_register()
            elif cmd == "3":
                self.exit()
            else:
                print("输入错误。")

    def do_sign_in(self):
        while True:
            name = input("输入用户名：")
            passwords = input("输入密码：")
            self.s.send(f"L {name} {passwords}".encode())
            data = self.s.recv(48)
            if data == b"no":
                print("登录失败。")
            elif data == b"yes":
                print("登录成功。")
                break
        while True:
            print("请输入相应的序号：<1、登录> <2、注册> <3.退出>")

    def do_register(self):
        while True:
            name = input("请输入姓名：")
            if " " in name:
                print("不能有空格，请重新输入。")
                continue
            self.s.send(f"R {name}".encode())
            data = self.s.recv(48)
            if data == b"no":
                print("用户名已存在，请重新输入。")
            elif data == b"yes":
                break
        while True:
            passwords = input("请输入密码：")
            if " " in name:
                print("不能有空格，请重新输入。")
                continue
            else:
                break
        self.s.send(f"R {name} {passwords}".encode())
        data = self.s.recv(48)
        if data == b"ok":
            print("注册成功。")
        return

    def exit(self):
        pass


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 2048
    dcv = DictClientView(host, port)
    dcv.main()
