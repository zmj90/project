"""
练习2: 创建数据库 dict  创建数据表 words (id  word   mean)
      将单词本中的单词存入到数据表中

create database dict charset=utf8;

create table words (
id int primary key auto_increment,
word char(30),
mean varchar(512));
"""

import pymysql
import re
# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 创建游标（调用sql语句，获取执行结果）
cur = db.cursor()

# 查询语句
file = open('../../day03/dict.txt')
for line in file:
    # print(line)
    word_mean=re.findall(r"(\w+)\s+(.*)",line)[0]

    try:
        sql = "insert into words (word,mean) values(%s,%s)"
        cur.execute(sql, word_mean)
        db.commit()
    except Exception as e:
        db.rollback()
file.close()
# 关闭游标和数据库
cur.close()
db.close()
