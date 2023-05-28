import pymysql

# 链接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password='123456',
                     database="Image",
                     charset="utf8")
# 创建游标对象
cur = db.cursor()

# 打开文件
file = open("cad.jpg", "rb")
data = file.read()
# print(data)

# 插入数据
sql = "insert into image (name,picture) values (%s,%s)"
name = "cad"
cur.execute(sql, [name, data])
db.commit()

# 关闭游标、数据库
cur.close()
db.close()
# 关闭文件
file.close()
