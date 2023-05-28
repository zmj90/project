"""
3. 写一个程序，input输入一个设备名称，从文档中提取出这个设备的address is值
        打印出来

         提示： 每一段之间有空行
               设备名称是每一段的第一个单词
               每一段都有address is
"""
import re




def find_id():
    file = open("../../day04/log.txt")
    is_exist(file)
    re =print_result(file)
    file.close()
    return re

def print_result(file):
    pattern2 = r"[/\w]{1,4}\.[/\w]{1,4}\.[/\w]{1,4}(\.[/\w]{1,4})?\b"
    while True:
        date = file.readline()
        if date == "\n":
            return "address is Unknown"
        try:
            date_id = re.search(pattern2, date).group()
        except Exception:
            continue
        else:
            if date_id:
                return "address is:%s" % date_id


def is_exist(file):
    pattern1 = r"^[-/\.\w]+\b"
    a = False
    while True:
        equip_name = input("输入设备名称：")
        file.seek(0, 0)
        for line in file:
            name = re.findall(pattern1, line)
            if name == [equip_name]:
                a = True
                break
        else:
            print("没有该设备-----需重新输入")
        if a:
            break


if __name__ == "__main__":
    print(find_id())