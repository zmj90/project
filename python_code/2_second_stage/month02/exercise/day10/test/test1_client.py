from socket import *

HOST = "localhost"
PORT = 2048
ADDRESS = (HOST, PORT)

s = socket(2, 2)

s.sendto(b"hello", ADDRESS)

data, address = s.recvfrom(1024)
print(data.decode())

s.close()