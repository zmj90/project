from socket import *
from threading import Thread
import os, sys
from time import sleep

ADDRESS = ("0.0.0.0", 2048)
ftp = "../../day14/"


class FtpServer(Thread):
    def __init__(self, con_fd, flag):
        super(FtpServer, self).__init__(daemon=flag)
        self.con_fd = con_fd

    def run(self):
        while True:
            data = self.con_fd.recv(128).decode()
            if not data or data == "Q":
                print("客户端退出了")
                return
            elif data == "L":
                self.do_look()
                continue
            msg = data.split(" ")
            if msg[0] == "G":
                self.do_download(msg[1])
            elif msg[0] == "P":
                self.do_upload(msg[1])

    def do_look(self):
        file_list = os.listdir(ftp)
        if not file_list:
            self.con_fd.send(b"no")
        else:
            self.con_fd.send(b"yes")
        sleep(0.1)
        file_str = "\n".join(file_list).encode()
        self.con_fd.send(file_str)

    def do_download(self, file_name):
        if os.path.exists(f"{ftp}{file_name}"):
            self.con_fd.send(b"yes")
        else:
            self.con_fd.send(b"no")
            return
        sleep(0.1)
        file = open(f"{ftp}{file_name}", "rb")
        while True:
            data = file.read(1024)
            if not data:
                sleep(0.1)
                self.con_fd.send(b"@@")
                break
            self.con_fd.send(data)
        file.close()

    def do_upload(self, file_name):
        file_name = file_name.split("/")[-1]
        if os.path.exists(f"{ftp}{file_name}"):
            self.con_fd.send(b"no")
            return
        else:
            self.con_fd.send(b"yes")
        file = open(f"{ftp}{file_name}", "wb")
        while True:
            data = self.con_fd.recv(1024)
            if data == b"@@":
                break
            file.write(data)
        file.close()


def main():
    s = socket()
    s.bind(ADDRESS)
    s.listen(3)

    while True:
        try:
            con_fd, address = s.accept()
            print(f"{address} 已连接")
        except KeyboardInterrupt:
            sys.exit()
        t = FtpServer(con_fd, True)
        t.start()


if __name__ == '__main__':
    main()