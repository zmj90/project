from socket import *
from select import select
import re
from typing import *

class HttpServer:
    def __init__(self, host="localhost", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.s = socket()
        self.s.setblocking(False)
        self.s.bind((self.host, self.port))
        self.r_list = []
        self.w_list = []
        self.x_list = []

    def start(self):
        self.s.listen(3)
        self.r_list.append(self.s)
        while True:
            rs, ws, xs = select(self.r_list,self.w_list,self.x_list)
            for r in rs:
                if r == self.s:
                    c, addr = r.accept()
                    print(addr)
                    c.setblocking(False)
                    self.r_list.append(c)
                else:
                    self.handle(r)

    def handle(self, r: socket):
        data = r.recv(1024).decode()
        pattern = r"[A-Z]+\s(/\S*)"
        try:
            info = re.match(pattern,data).group(1)
        except:
            self.r_list.remove(r)
            r.close()
        else:
            self.get_html(r, info)

    def get_html(self, r, info):
        if info == "/":
            filename = f"{self.html}/index.html"
        else:
            filename = f"{self.html}{info}"
        try:
            file = open(filename, "rb")
            data = file.read()
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response_content = "<h1>Sorry......</h1>"
            msg = response + response_content
            r.send(msg.encode())
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += f"Content-Length:{len(data)}\r\n"
            response += "\r\n"
            msg = response.encode() + data
            r.send(msg)
            file.close()


if __name__ == '__main__':
    host = "0.0.0.0"
    port = 2048
    html = "./static"

    hs = HttpServer(host, port, html)
    hs.start()
