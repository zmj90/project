"""
数据库查询示例
"""

import pymysql

# 链接数据库
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user="root",
                     password='123456',
                     database="stu",
                     charset="utf8")

# 创建游标 (调用sql语句,获取执行结果)
cur = db.cursor()

# 查询数据
sql = "select name,age,sex,score from cls where score > 70;"
cur.execute(sql)

# 第一种
# for i in cur:
#     print(i) # 一条查询记录

# 第二种
# for i in range(cur.execute(sql)):
one = cur.fetchone()
print(one)
#
# many = cur.fetchmany(2)
# print(many)

# all = cur.fetchall()
# print(all)

# 关闭游标和数据库
cur.close()
db.close()