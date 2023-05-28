from socket import *
import sys
from time import sleep

ADDRESS = ("0.0.0.0", 2048)
ftp = "../file/"


class FtpClient:
    def __init__(self, s):
        self.s = s

    def do_look(self):
        self.s.send(b"L")
        data = self.s.recv(128)
        if data == b"no":
            print("没有文件")
        elif data == b"yes":
            data = self.s.recv(2048).decode()
            print(data)

    def do_download(self, file_name):
        self.s.send(f"G {file_name}".encode())
        data = self.s.recv(128)
        if data == b"no":
            print("输入错误")
        elif data == b"yes":
            file = open(f"{ftp}{file_name}", "wb")
            while True:
                data = self.s.recv(1024)
                if data == b"@@":
                    break
                file.write(data)
            file.close()

    def do_upload(self, file_name):
        self.s.send(f"P {file_name}".encode())
        data = self.s.recv(128)
        if data == b"no":
            print("已有")
        elif data == b"yes":
            sleep(0.1)
            file = open(f"{file_name}", "rb")
            while True:
                data = file.read(1024)
                if not data:
                    sleep(0.1)
                    self.s.send(b"@@")
                    break
                self.s.send(data)
            file.close()

    def do_exit(self):
        self.s.send(b"Q")
        sys.exit()


def main():
    s = socket()
    s.connect(ADDRESS)

    f = FtpClient(s)

    while True:
        print("<l> <g file> <p file> <q>")
        try:
            msg = input(">>> ")
        except KeyboardInterrupt:
            sys.exit()
        if msg == "l":
            f.do_look()
        elif msg[0] == "g":
            f.do_download(msg.split(" ")[1])
        elif msg[0] == "p":
            f.do_upload(msg.split(" ")[1])
        elif msg == "q":
            f.do_exit()
        else:
            print("输错了.................")


if __name__ == '__main__':
    main()