from socket import *

ADDRESS = ("0.0.0.0", 2049)

s = socket()
s.bind(ADDRESS)
s.listen(3)
print("允许客户端链接")

con_fd, address = s.accept()
print(f"{address} 链接上了")
print(con_fd)
data = con_fd.recv(1024)
print(data)
con_fd.send(b"ok")

con_fd.close()
s.close()