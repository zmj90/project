"""
作业 :  2. 编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端
           服务端     接收内容 --> 写入到一个文件中
           客户端     读取图片内容  --> 发送给服务端
"""
from socket import *


class FileManager:
    def __init__(self):
        self.file = open("./2.jpg", "rb")

    def read_out(self):
        data = self.file.read(1024)
        return data


def main():
    tcp_socket = socket()
    try:
        server_address = ("localhost", 2048)
        tcp_socket.connect(server_address)
        fm = FileManager()
        while True:
            data = fm.read_out()
            if not data:
                tcp_socket.send("上传完毕".encode())
                print("上传完毕")
            else:
                tcp_socket.send(data)
                print("发送", data)
            tcp_socket.recv(20)
            print("收到")
            if not data:
                break
        tcp_socket.close()
    except ConnectionRefusedError:
        return


if __name__ == "__main__":
    main()
