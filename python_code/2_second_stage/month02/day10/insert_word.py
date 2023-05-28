"""
练习2: 创建数据库 dict  创建数据表 words (id  word   mean)
      将单词本中的单词存入到数据表中

create database dict charset=utf8;

create table words (id int primary key auto_increment,word char(30),mean varchar(512));
"""

import pymysql
import re

# 链接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password='123456',
                     database="dict",
                     charset="utf8")

# 创建游标 (调用sql语句,获取执行结果)
cur = db.cursor()

# 数据操作
args_list = []  #  [(x,xxxx),(x,xxxxx).......]
f = open('dict.txt')

for line in f:
    # 提取单词和解释
    t = re.findall(r"(\w+)\s+(.*)",line)[0]
    args_list.append(t)

sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()



# 关闭游标和数据库
cur.close()
db.close()