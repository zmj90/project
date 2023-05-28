"""
思路:
1. 输入学生信息
2. 将学生信息发送给服务端
"""


from socket import *

# 访问服务端需要的地址
server_addr = ('127.0.0.1',8888)

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        try:
            # 具体做的事情
            print("===================================================")
            name = input("Name:")
        except KeyboardInterrupt:
            break
        age = input("Age:")
        sex = input("Sex:")
        score = input("Score:")
        data = "%s %s %s %s"%(name,age,sex,score)
        udp_socket.sendto(data.encode(),server_addr) # 学生信息发送


    udp_socket.close()

main()

