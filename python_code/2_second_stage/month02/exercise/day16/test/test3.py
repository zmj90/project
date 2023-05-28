from select import *
from socket import *

s = socket()
s.bind(("0.0.0.0", 2048))
s.listen(3)
s.setblocking(False)

p_dict = {s.fileno(): s}

pl = poll()
pl.register(s, POLLIN)

while True:
    events = pl.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, address = s.accept()
            print(f"{address} 已连接")
            c.setblocking(False)
            p_dict[c.fileno()] = c
            pl.register(c, POLLIN)
        else:
            data = p_dict[fd].recv(1024)
            if not data:
                del p_dict[fd]
                p_dict[fd].close()
                pl.unregister(fd)
                continue
            print(data)
            p_dict[fd].send(b'OK')
