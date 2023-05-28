import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 创建游标（调用sql语句，获取执行结果）
cur = db.cursor()

# 查询语句
name = input('请输入姓名:')
sql = "select score from cls where name = %s"
cur.execute(sql,name)
print(cur.fetchone()[0])
# 关闭游标和数据库
cur.close()
db.close()
