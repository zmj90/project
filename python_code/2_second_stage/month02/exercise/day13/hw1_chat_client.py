from socket import *
from multiprocessing import Process, Queue
from time import sleep

# 服务器地址
ADDRESS = ('127.0.0.1', 2048)


# 发送请求
def transmit(s, name, q):
    """
    s: udp套接字
    name: 聊天人的名字
    q: 消息队列对象
    """
    while True:
        try:
            msg = input(">>> ")
        except KeyboardInterrupt:
            msg = "quit"
        if msg == "quit":
            s.sendto(f"Q {name}".encode(), ADDRESS)
            return
        s.sendto(f"C {name} {msg}".encode(), ADDRESS)
        sleep(0.1)
        # 被服务端踢出聊天室，退出父进程
        try:
            data = q.get(False)
        except:
            data = None
        if data == "ok":
            return


# 接收响应
def receive(s: socket,q: Queue):
    while True:
        data, address = s.recvfrom(2048)
        if data == b"no":
            print("你被请出了聊天室。")
            q.put("ok")
        else:
            print(f"\n{data.decode()}\n>>> ", end="")


def main():
    """
    启动函数
    """
    s = socket(2, 2)
    q = Queue(3)

    while True:
        name = input("输入姓名进入聊天室：")
        msg = f"E {name}".encode()
        s.sendto(msg, ADDRESS)
        data, address = s.recvfrom(50)
        if data == b"ok":
            break
        if data == b"no":
            print("你被拉入了黑名单。")
            return
        print(data.decode())

    p = Process(target=receive, args=(s,q), daemon=True)
    p.start()

    transmit(s, name, q)


if __name__ == '__main__':
    main()


