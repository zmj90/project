"""
思路:
1. input 输入一个单词
2. 将单词发送给服务端
3. 从服务端接收回发的结果,打印出来
"""

from socket import *

# 访问服务端需要的地址
server_addr = ('127.0.0.1',8888)

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        word = input("你要查询的单词:")
        if not word:
            break
        udp_socket.sendto(word.encode(),server_addr) # 发送单词
        # 接收解释
        data,addr = udp_socket.recvfrom(1024)
        print("%s : %s"%(word,data.decode()))

    udp_socket.close()

main()

