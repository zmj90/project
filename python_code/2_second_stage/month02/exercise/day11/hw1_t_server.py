"""
作业 :  2. 编写一个程序, 使用tcp完成. 从客户端上传一个头像(图片) 到服务端
           服务端     接收内容 --> 写入到一个文件中
           客户端     读取图片内容  --> 发送给服务端
"""
from socket import *


class FileManager:
    def __init__(self):
        self.file = open("./风景.jpg", "wb")

    def write_in(self, data):
        self.file.write(data)


def main():
    tcp_socket = socket()
    tcp_socket.bind(("localhost", 2048))
    tcp_socket.listen(6)
    try:
        while True:
            print(">>>")
            connect_socket, address = tcp_socket.accept()
            fm = FileManager()
            while True:
                data = connect_socket.recv(1024)
                print("收到", data)
                if data == "上传完毕".encode():
                    connect_socket.send("已存入".encode())
                    print("已存入")
                    break
                else:
                    fm.write_in(data)
                    # fm.file.seek(0, 2)
                    connect_socket.send(b">")
                    print("发送")
            connect_socket.close()
    except KeyboardInterrupt:
        tcp_socket.close()
        return


if __name__ == '__main__':
    main()