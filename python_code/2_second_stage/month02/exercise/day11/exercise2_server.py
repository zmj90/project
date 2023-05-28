"""
使用udp套接字编程完成

从客户端,input输入一个单词,发送给服务端
从服务端,回发给客户端这个单词的解释,并在客户端打印一下

单词使用 dict数据查询
"""
from socket import *
import pymysql


class UdpSocket:
    def __init__(self):
        self.u_sk = socket(AF_INET, SOCK_DGRAM)
        self.u_sk.bind(("localhost", 2048))
        self.db = DataBase()

    def rf_st(self):
        while True:
            try:
                data, address = self.u_sk.recvfrom(30)
            except KeyboardInterrupt:
                return
            one = self.db.find_word(data)
            self.u_sk.sendto(one, address)

    def close(self):
        self.db.close()
        self.u_sk.close()


class DataBase:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def find_word(self, word):
        sql = "select mean from words where word = %s;"
        self.cur.execute(sql, [word.decode()])
        one = self.cur.fetchone()
        if not one:
            return "没有该单词。".encode()
        return one[0].encode()

    def close(self):
        self.cur.close()
        self.db.close()


def main():
    us = UdpSocket()
    us.rf_st()


if __name__ == "__main__":
    main()
