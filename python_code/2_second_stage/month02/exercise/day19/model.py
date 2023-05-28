import pymysql


class DictServerModel:
    id_word = 0

    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password='123456',
                                  database="dict",
                                  charset="utf8")
        self.cur = self.db.cursor()

    def add_username(self, name, passwords):
        sql = f"insert into username (name, passwords) values ({name}, {passwords});"
        try:
            self.cur.execute(sql,(name, passwords))
            self.db.commit()
        except:
            self.db.rollback()

    def close(self):
        self.cur.close()
        self.db.close()

    def select_mean(self, word):
        sql = f"select id, mean from words word = {word}"
        self.cur.execute(sql, [word])
        one = self.cur.fetchone()
        DictServerModel.id_word = one[0]
        return one[1]

    def add_history_log(self, name, time):
        sql = f"select id from username name = {name}"
        self.cur.execute(sql, (name,))
        nid = self.cur.fetchone()
        wid = DictServerModel.id_word
        sql = f"insert into words_username (wid, nid, select_time) values ({wid}, {nid}, {time});"
        try:
            self.cur.execute(sql, (wid, nid, time))
            self.db.commit()
        except:
            self.db.rollback()

    def select_history_log(self):
        pass