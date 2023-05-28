"""
使用udp套接字编程完成

从客户端,input输入一个单词,发送给服务端
从服务端,回发给客户端这个单词的解释,并在客户端打印一下

单词使用 dict数据查询

思路 :
1. 接收到客户端的单词
2. 通过数据库查找到单词(如果查不到怎么办)
3. 将单词查询结果发送给客户端

"""

from socket import *
import pymysql

# 数据库功能类
class Database:
    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             password='123456',
                             database="dict",
                             charset="utf8")

        # 创建游标 (调用sql语句,获取执行结果)
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    # 查单词
    def find_word(self,word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql,[word])

        mean = self.cur.fetchone()
        if mean:
            # 如果找到了
            return mean[0]
        else:
            # 没找到
            return "Not Found The Word!"



def main():
    udp_socket =  socket(AF_INET,SOCK_DGRAM) # 创建套接字
    udp_socket.bind(("0.0.0.0",8888)) # 绑定地址
    db = Database()  # 实例化对象

    while True:
        try:
            data,addr = udp_socket.recvfrom(50) # 接收单词
            mean = db.find_word(data.decode()) # 找单词
            udp_socket.sendto(mean.encode(),addr) # 发送结果
        except KeyboardInterrupt:
            break

    db.close()
    udp_socket.close()
    print("服务结束")


main()












