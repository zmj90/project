"""
练习: 编写一个程序,将index.html这个网页通过浏览器访问并且展示
"""

from socket import *

response = """HTTP/1.1 200 OK
Content-Type:text/html

"""

def request(con_fd):
    data = con_fd.recv(1024)

    file = open("index.html")
    info = file.read()
    file.close()

    info = f"{response}\r\n{info}"

    con_fd.send(info.encode()) # 发送给客户端
    con_fd.close()


def main():
    s = socket()
    s.bind(('0.0.0.0',2048))
    s.listen(3)

    while True:
        con_fd, address = s.accept()
        print("Connect from",address)
        request(con_fd)


if __name__ == '__main__':
    main()