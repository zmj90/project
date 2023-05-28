"""
写入数据库示例2
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

# 写数据操作
l = [
    ('Dave',15,'m',81),
    ('Ala',16,'w',82),
    ('Baron',17,'m',83)
]
try:
    sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"

    # for i in l:
    #     cur.execute(sql,i)

    cur.executemany(sql,l) # 执行多次sql语句

    db.commit()   # 提交
except Exception as e:
    print(e)
    db.rollback() # 回滚



# 关闭游标和数据库
cur.close()
db.close()