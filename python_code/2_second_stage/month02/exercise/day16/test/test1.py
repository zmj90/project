from socket import *
from time import ctime,sleep

f = open('net.log','a+')
s = socket()
s.bind(("localhost", 2048))
s.listen()

s.setblocking(False)

while True:
    print("Waiting for connect...")
    try:
        con_fd, address = s.accept()  # 阻塞
        print("Connect from", address)
    except BlockingIOError as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    else:
        data = con_fd.recv(1024)
        print(data)
