from socket import *
import pymysql


def select_mean(word):
    db = pymysql.connect(host="localhost",
                         port=3306,
                         user="root",
                         password='123456',
                         database="dict",
                         charset="utf8")
    cur = db.cursor()
    sql = "select mean from words where word=%s limit 1;"
    cur.execute(sql, [word.decode()])
    one = cur.fetchone()[0]
    cur.close()
    db.close()
    return one


udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("localhost", 2048))
data, address = udp_socket.recvfrom(30)
one = select_mean(data)
udp_socket.sendto(one.encode(), address)
udp_socket.close()

udp_socket = socket(AF_INET,SOCK_DGRAM)