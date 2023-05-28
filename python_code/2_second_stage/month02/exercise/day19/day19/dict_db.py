"""
数据处理模块

* 根据dict_server的指令获取数据
* 与数据库交互
"""

import pymysql


class DictServerModel:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password='123456',
                                  database="dict",
                                  charset="utf8")

    def cursor(self):
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def find_name(self, name):
        self.cursor()
        sql = "select name from user where name=%s;"
        self.cur.execute(sql,[name])
        one = self.cur.fetchone()
        print(one)
        if one:
            return False
        else:
            return True

    def add_user(self, name, passwords):
        sql = "insert into user (name, passwords) values (%s, %s);"
        try:
            self.cur.execute(sql,[name, passwords])
            self.db.commit()
        except:
            self.db.rollback()

    def sign_in(self,name, passwords):
        sql = "select name from user where name=%s and passwords=%S;"
        self.cur.execute(sql, [name, passwords])
        one = self.cur.fetchone()
        if one:
            return True
        else:
            return False
