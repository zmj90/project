from socket import *
from select import *
from typing import Dict


class DictServerController:
    def __init__(self, host=None, port=80):
        self.host = host
        self.port = port
        self.s = socket()
        self.s.setblocking(False)
        self.s.bind((self.host, self.port))

        self.map_fd: Dict[int, socket] = {}

    def start(self):
        self.s.listen()
        self.map_fd[self.s.fileno()] = self.s
        ep = epoll()
        ep.register(self.s, EPOLLIN)
        while True:
            events = ep.poll()
            for fd, event in events:
                if fd in self.map_fd:
                    c, address = self.map_fd[fd].accept()
                    self.map_fd[c.fileno()] = c
                    ep.register(c, EPOLLIN)
                    c.setblocking(False)
                else:
                    self.handle(self.map_fd[fd])

    def handle(self, c):
        data = c.recv(128).decode()
        msg = data.split(" ")
        if msg[0] == "L":
            pass

