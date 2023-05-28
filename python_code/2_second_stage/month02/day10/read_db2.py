"""
数据库查询示例2
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
# name = input(">>")
# sql = "select score from cls where name='%s';"%name
# print(sql)
# cur.execute(sql)
# print(cur.fetchone())

# 通过列表为sql语句传入数据
name = input(">>")
sql = "select name,score from cls where name = %s or score > %s;"
cur.execute(sql,[name,85])  # 列表是不能传递表明 字段名 关键字
print(cur.fetchall())


# 关闭游标和数据库
cur.close()
db.close()