import pymysql
import re

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password='123456',
                     database="dict",
                     charset="utf8")
# 创建游标对象
cur = db.cursor()

# 将词典存入列表
args_list = []
file = open("dict.txt")
for line in file:
    t = re.findall(r"(\w+)\s+(.*)", line)[0]
    args_list.append(t)

# 插入数据
sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, args_list)
    db.commit()
except:
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
