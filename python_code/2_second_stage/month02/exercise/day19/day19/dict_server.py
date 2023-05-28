"""
dict 服务端

* 接收客户端请求
* 进行请求处理
* 向客户端发送结果
"""

from socket import *
from multiprocessing import Process
import sys
from signal import *
from day19.dict_db import *


class MyProcess(Process):
    def __init__(self, c: socket, db: DictServerModel):
        super().__init__()
        self.c = c
        self.db = db

    def run(self):
        while True:
            data = self.c.recv(128).decode()
            msg = data.split(" ")
            if msg[0] == "R":
                self.do_register(msg)
            elif msg[0] == "L":
                self.do_sign_in(msg)

    def do_register(self, msg):
        if not self.db.find_name(msg[1]):
            self.c.send(b"no")
        else:
            self.c.send(b"yes")
            data = self.c.recv(128).decode()
            msg = data.split(" ")
            self.db.add_user(msg[1], msg[2])
            self.c.send(b"ok")

    def do_sign_in(self, msg):
        if self.db.sign_in(msg[1], msg[2]):
            self.c.send(b"yes")
        else:
            self.c.send(b"no")



class DictServerController:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket()
        self.s.bind((self.host, self.port))

    def main(self):
        self.s.listen(3)
        print(f"listen the port {self.port}")
        signal(SIGCHLD, SIG_IGN)
        db = DictServerModel()
        while True:
            try:
                c, address = self.s.accept()
                print(address)
            except:
                self.s.close()
                sys.exit("服务端退出")
            p = MyProcess(c, db)
            p.daemon = True
            p.start()


if __name__ == '__main__':
    host = "0.0.0.0"
    port = 2048
    dsc = DictServerController(host, port)
    dsc.main()
