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
            print("等待链接")
            connect_socket, address = tcp_socket.accept()
            fm = FileManager()
            while True:
                data = connect_socket.recv(1024)
                # print(data)
                if not data:
                    print("传输完成")
                    connect_socket.send(data)
                    print(data)
                    break
                fm.write_in(data)
                fm.file.seek(0, 2)
    except KeyboardInterrupt:
        tcp_socket.close()
        print("服务器已关闭。")
        return


if __name__ == '__main__':
    main()