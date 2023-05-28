"""
作业 :  2. 编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端
           服务端     接收内容 --> 写入到一个文件中
           客户端     读取图片内容  --> 发送给服务端
"""
from socket import *


class FileManager:
    def __init__(self):
        self.file = open("./1.jpg", "rb")

    def read_out(self):
        data = self.file.read(1024)
        return data


def main():
    tcp_socket = socket()
    server_address = ("localhost", 2048)
    fm = FileManager()
    try:
        tcp_socket.connect(server_address)
        while True:
            data = fm.read_out()
            if not data:
                tcp_socket.send(b"ok")
                print("图片上传完毕")
            else:
                tcp_socket.send(data)
            tcp_socket.recv(2)
            if not data:
                print("thank you!")
                break
        tcp_socket.close()
    except ConnectionRefusedError:
        print("服务器没有启动。")


if __name__ == "__main__":
    main()
