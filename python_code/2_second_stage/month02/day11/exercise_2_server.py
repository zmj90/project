"""

练习3 : 完成一个学生信息录取程序

        从客户端输入学生的姓名,年龄,性别,分数
        将输入的内容发送给服务端
        在服务端将学生信息存入到数据库的 stu --> cls表

思路:
1. 接收学生信息
2. 存储到数据库
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
                             database="stu",
                             charset="utf8")

        # 创建游标 (调用sql语句,获取执行结果)
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        # 关闭游标和数据库
        self.cur.close()
        self.db.close()

    # 插入数据 list_ -->[name,age,sex,score]
    def insert_data(self,list_):
        sql = "insert into cls (name,age,sex,score) value (%s,%s,%s,%s);"
        try:
            self.cur.execute(sql,list_)
            self.db.commit()
        except :
            self.db.rollback()


# 主函数启动程序
def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)  # 创建套接字
    udp_socket.bind(("0.0.0.0", 8888))  # 绑定地址
    db = Database()  # 实例化对象

    while True:
        try:
            # 具体做的事情 data--> b"name age sex score"
            data, addr = udp_socket.recvfrom(128)  # 接收学生信息
            info = data.decode().split(' ') # info -->[name,age,sex,score]
            db.insert_data(info)
        except KeyboardInterrupt:
            break

    db.close()
    udp_socket.close()
    print("服务结束")


main()