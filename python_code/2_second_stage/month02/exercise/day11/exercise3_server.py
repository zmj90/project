"""
练习3 : 完成一个学生信息录取程序

从客户端输入学生的姓名,年龄,性别,分数
将输入的内容发送给服务端
在服务端将学生信息存入到数据库的 stu --> cls表
"""
from socket import *
import pymysql


class Database:
    def __init__(self):
        # 链接数据库
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password='123456',
                                  database="stu",
                                  charset="utf8")

        # 创建游标 (调用sql语句,获取执行结果)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    def insert_message(self, message):
        sql = "insert into cls(name,age,sex,score) values(%s,%s,%s,%s);"
        try:
            self.cur.execute(sql, message)
            self.db.commit()
        except:
            self.db.rollback()


class Socket:
    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
        self.udp_socket.bind(("0.0.0.0", 2048))  # 绑定地址
        self.db = Database()  # 实例化对象

    def close(self):
        self.db.close()
        self.udp_socket.close()
        print("服务结束")

    def receive_sendto(self):
        while True:
            try:
                data, address = self.udp_socket.recvfrom(1024)
                self.db.insert_message(data.decode().split("-"))
                self.udp_socket.sendto("已录入。".encode(), address)
            except KeyboardInterrupt:
                return


def main():
    sk = Socket()
    sk.receive_sendto()
    sk.close()


if __name__ == "__main__":
    main()
