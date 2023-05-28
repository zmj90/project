"""
练习4: tcp完成,编写一个简单的机器人对话程序

      服务端和客户端,通过客户端可以与服务端对话

      你好 --> 你好!
      你叫什么 --> 我叫小美
      你几岁 --> 2岁啦

      如果提问无法识别则回复  --> "人家还小,听不懂啦."
"""

from socket import *


chat = {
    "你好":"你好!",
    "你叫什么":"我叫小美",
    "你几岁了":"2岁了"
}


# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)
# 绑定地址
tcp_socket.bind(("192.168.94.140",8888))
# 将套接字设置为监听套接字,监听队列大小为5
tcp_socket.listen(5)

print("等待客户端链接....")
# 等待处理客户端链接
connect_socket,addr = tcp_socket.accept()
print("链接了",addr,"客户端")  # 打印地址

# 接收消息
while True:
    data = connect_socket.recv(1024).decode()
    if data == '##':
        break

    if data in chat:
        connect_socket.send(chat[data].encode()) # 发送对话
    else:
        connect_socket.send("人家还小,听不懂啦.".encode())

# 关闭套接字
connect_socket.close()
tcp_socket.close()

