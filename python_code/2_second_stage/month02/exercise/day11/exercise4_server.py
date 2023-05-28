from socket import *

# 1.创建tcp套接字
tcp_socket = socket()
# 2.绑定地址
tcp_socket.bind(("192.168.0.103",2050))
# 3.将套接字设置为监听套接字,监听队列大小为5
tcp_socket.listen(5)
# 4.等待处理客户端链接
connect_socket,address = tcp_socket.accept()
# 5.6接收消息
while True:
    data = connect_socket.recv(20)
    if not data:
        break
    dict_ = {"你好":"你好!","你叫什么":"我叫小美","你几岁":"2岁了"}
    if data.decode() in dict_:
        result = dict_[data.decode()].encode()
    else:
        result = "人家还小，听不懂。".encode()
    connect_socket.send(result)
# 7.关闭套接字
connect_socket.close()
tcp_socket.close()
