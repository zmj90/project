from socket import *

s = socket()
print(type(s))
print(s)
s.bind(("0.0.0.0", 2048))
s.listen(3)
c, addr = s.accept()
print(type(c))
print(c)
