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
        # if not data:
            # print(type(data))
            # print(data)
        return data


def main():
    tcp_socket = socket()
    server_address = ("localhost", 2048)
    try:
        tcp_socket.connect(server_address)
    except ConnectionRefusedError:
        print("服务器没有运行。")
        tcp_socket.close()
        return
    fm = FileManager()
    while True:
        data = fm.read_out()
        tcp_socket.send(data)
        if not data:
            print("上传成功。")
            break
    print(data)
    # data1 = tcp_socket.recv(1024)
    # if not data1:
    #     tcp_socket.close()


if __name__ == "__main__":
    main()
