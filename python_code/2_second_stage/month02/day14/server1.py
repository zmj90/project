from socket import *
from multiprocessing import Process
from signal import *

HOST = "0.0.0.0"
PORT = 8888
ADDRESS = (HOST, PORT)



def handle(connfd):
    pass


def main():
    sock = socket()
    sock.bind(ADDRESS)
    sock.listen(3)

    signal(SIGCHLD, SIG_IGN)

    while True:
        connfd, address = sock.accept()
        print("客户端地址", address)

        p = Process(target=handle, args=(connfd,))
        p.start()


if __name__ == '__main__':
    main()
