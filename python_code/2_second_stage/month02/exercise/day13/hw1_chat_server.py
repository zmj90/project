"""
聊天室 服务端
功能 ： 类似qq群功能
【1】 有人进入聊天室需要输入姓名，姓名不能重复
【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
聊天室代码扩展
增加敏感词汇 : xx aa bb oo
当有成员聊天内容中包含敏感词汇，则进行屏蔽，并且向群里 发出对xxx的警告信息
如果一个人被警告三次则踢出该群，同时拉黑这个地址
"""
from socket import *
from multiprocessing import Process
from time import sleep

# 服务器地址
ADDRESS = ("127.0.0.1", 2048)
# {name:address}服务端
dict_user = {}
# 敏感词汇
words = ("aa", "bb", "cc", "oo", "xx")
# 警告次数{name:count}
dict_count = {}
# 禁用地址ip
list_address = []


# 进入聊天室
def do_in(s, name, address):
    """
    s: udp套接字
    name: 聊天人的名字
    address: 相应的地址
    """
    if address[0] in list_address:
        s.sendto(b"no", address)
        return
    if name in dict_user or "管理" in name:
        s.sendto("该用户名已存在,请重新输入。".encode(), address)
    else:
        s.sendto(b"ok", address)
        for key in dict_user:
            s.sendto(f"欢迎{name}进入聊天室".encode(), dict_user[key])
        dict_user[name] = address


# 审查
def do_check(msg):
    """
    msg: 聊天信息
    """
    for item in words:
        if item in msg:
            return False
    return True


# 管理用户
def do_user(name, s):
    """
    s: udp套接字
    name: 聊天人的名字
    """
    for key in dict_user:
        s.sendto(f"{name}请注意你的言词。".encode(), dict_user[key])
    if name in dict_count:
        dict_count[name] += 1
        if dict_count[name] == 3:
            list_address.append(dict_user[name][0])
            s.sendto(b"no", dict_user[name])
            del dict_user[name]
            del dict_count[name]
            sleep(0.1)
            for key in dict_user:
                    s.sendto(f"管理员将违规者{name}踢出了群聊。".encode(), dict_user[key])
    else:
        dict_count[name] = 1


# 聊天
def do_chat(s, name, msg, address):
    """
    s: udp套接字
    name: 聊天人的名字
    msg: 相应的信息
    address: 相应的地址
    """
    if address[0] in list_address:
        s.sendto(b"no", address)
        return
    if not do_check(msg):
            do_user(name, s)
    else:
        for key in dict_user:
            if name != key:
                s.sendto(f"{name}:{msg}".encode(), dict_user[key])


# 退出聊天室
def do_out(s, name):
    """
    s: udp套接字
    name: 聊天人的名字
    """
    if name in dict_user:
        del dict_user[name]
        for key in dict_user:
            s.sendto(f"{name}退出了聊天室。".encode(), dict_user[key])


# 管理员
def manager(s):
    """
    s: udp套接字
    """
    while True:
        try:
            msg = input("管理员：")
        except KeyboardInterrupt:
            break
        s.sendto(f"C 管理员 {msg}".encode(), ADDRESS)


# 处理客户端的请求
def handle_request(s: socket):
    while True:
        try:
            data, address = s.recvfrom(2048)
        except KeyboardInterrupt:
            break
        msg = data.decode().split(" ", 2)
        if msg[0] == "E":  # 进入聊天室
            do_in(s, msg[1], address)
        elif msg[0] == "C":  # 聊天
            do_chat(s, msg[1], msg[2], address)
        elif msg[0] == "Q":  # 退出聊天室
            do_out(s, msg[1])


def main():
    """
    启动函数
    """
    s = socket(2, 2)
    s.bind(ADDRESS)

    p = Process(target=handle_request, args=(s,), daemon=True)
    p.start()

    manager(s)


if __name__ == '__main__':
    main()
