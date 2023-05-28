import logging

import pymysql.cursors


# Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='123456',
#                              database='test',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor
#                              )
#
# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster01@python.org', 'very-secret01'))
#         # ins = 'insert into filmtab values(%s,%s,%s)'
#         # cursor.execute(ins, ['霸王别姬', '张国荣', '1993'])
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     # connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email` like %s"
#         cursor.execute(sql, ('%webmaster%',))
#         result = cursor.fetchone()
#         # result = cursor.fetchmany(2)
#         # result = cursor.fetchall()
#         print(result, type(result))

class DataBase:
    """
    操作数据库
    """

    def __init__(self, date_base, fmt=True):
        """

        :param date_base: 数据库
        :param fmt: 查询时，返回() or ((),()) or {} or [{}, {}]
        """
        self.db = pymysql.connect(**date_base)
        self.cursor = self.db.cursor(
            cursor=pymysql.cursors.DictCursor if fmt else pymysql.cursors.Cursor
        )

    def close(self):
        """
        关闭数据库连接和操作对象
        :return: None
        """
        self.cursor.close()
        self.db.close()

    def execute(self, sql, args=None, flag=True):
        """

        :param sql: sql
        :param args: sql中的替代值，也可以不需要
        :param flag: if true 执行1条sql
        :return: Number of affected rows
        """
        try:
            if flag:
                logging.info(f"sql语句:{self.cursor.mogrify(sql, args)}")
                rows = self.cursor.execute(sql, args=args)
            else:
                for arg in args:
                    logging.info(f"sql语句:{self.cursor.mogrify(sql, arg)}")
                rows = self.cursor.executemany(sql, args=args)
            self.db.commit()
            return rows
        except Exception as e:
            self.db.rollback()
            logging.exception(e)

    def fetch(self, sql, args=None, flags=0, num=None):
        """
        查询结果
        :param sql: sql
        :param args: 可有可无，使用format也行
        :param flags: 为0，查询1条；为查询多条；其他查询所有
        :param num: 查询数量
        :return: () or ((),()) or {} or [{}, {}]
        """
        self.execute(sql, args=args)
        if flags == 0:
            res = self.cursor.fetchone()
        elif flags == 1:
            res = self.cursor.fetchmany(num)
        else:
            res = self.cursor.fetchall()
        logging.debug(f"查询结果：{res}，类型：{type(res)}")
        return res


db = DataBase
