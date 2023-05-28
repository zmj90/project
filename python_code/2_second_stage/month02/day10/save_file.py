"""
存储二进制文件

准备工作
alter table cls add image mediumblob;
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

# 存入文件
# f = open('mm.jpg','rb')
# data = f.read()
#
# try:
#     sql = "update cls set image=%s where name='Abby';"
#     cur.execute(sql,[data])
#     db.commit()
# except:
#     db.rollback()

# 提取文件
sql = "select image from cls where name='Abby';"
cur.execute(sql)
data = cur.fetchone() # 返回元祖
f = open('sjch.jpg','wb')
f.write(data[0])


f.close()
# 关闭游标和数据库
cur.close()
db.close()