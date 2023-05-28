"""
      2. 向一个文件中每隔2秒写入一行内容

         1. 2020-01-01  10:10:10
         2. 2020-01-01  10:10:12
         3. 2020-01-01  10:10:14
         4. 2020-01-01  10:10:16
         5. 2020-01-01  10:15:17
         6. 2020-01-01  10:15:19

         * 写入的内容可以实时看到
         * 程序终止后如果重新启动，序号能够衔接

         温馨提示：  from time import sleep
                    sleep(2)

"""
from time import sleep, ctime


def get_log():
    file = open("my_log", "a+", 1)
    file.seek(0, 0)
    n = len(file.readlines())
    while True:
        n += 1
        sleep(2)
        file.write(str(n) + ctime() + "\n")


get_log()