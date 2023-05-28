from socket import *

ADDRESS = ("127.0.0.1", 2049)

s = socket()
s.connect(ADDRESS)

s.send(b"hello")
data = s.recv(1024)
print(data)

s.close()
