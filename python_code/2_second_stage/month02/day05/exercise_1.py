"""
写一个程序，input输入一个设备名称，从文档中提取出这个设备的address is值
        打印出来

         提示： 每一段之间有空行
               设备名称是每一段的第一个单词
               每一段都有address is
"""

import re


# 获取目标段落 （生成器，每次生成一段内容）
def get_info():
    f = open("log.txt")
    while True:
        info = ""
        for line in f:
            if line == '\n':
                break
            else:
                info += line

        if not info:
            # 文件结尾
            f.close()
            return
        else:
            yield info


name = input("设备名称：")

# 每次获取一段内容(data)
for data in get_info():
    obj = re.match(r"\S+",data)  # 从一段内容中匹配首个单词
    if name == obj.group():
        # 找到了该找的段落 匹配地址
        pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
        obj = re.search(pattern,data)
        if obj:
            print(obj.group())
        else:
            # 没有匹配到
            print("该设备没有address")
        break
else:
    print("没有该设备")















