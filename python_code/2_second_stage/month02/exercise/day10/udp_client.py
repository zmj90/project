from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
server_address = ("localhost",2048)
word = input(">> ")
udp_socket.sendto(word.encode(),server_address)
data,addr = udp_socket.recvfrom(1024)
print(data.decode())
udp_socket.close()