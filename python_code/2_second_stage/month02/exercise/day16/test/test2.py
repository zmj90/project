from select import select
from socket import *

s = socket()
s.bind(("0.0.0.0", 2048))
s.listen(3)
s.setblocking(False)

r_list = [s]
w_list = []
x_list = []

while True:
    rs, ws, xs = select(r_list, w_list, x_list)
    for r in rs:
        if r is s:
            c, address = r.accept()
            print(f"{address} 已连接")
            r_list.append(c)
            c.setblocking(False)
        else:
            data = r.recv(1024)
            if not data:
                r_list.remove(r)
                r.close()
                continue
            r.send(b"ok")
