"""
重点代码
练习4： 文件的拷贝
       有一个文件  timg.jpeg,将其拷贝一份到主目录下，命名为 mm.jpg

       从源文件读取，写入到目标文件

思路 ： 从timg.jpeg中读取内容，原样写入到mm.jpg
"""


def copy():
    file1 = open("mm.jpg", "rb")
    file2 = open("美女.jpg", "wb")
    while True:
        data = file1.read(1024)
        if not data:
            break
        file2.write(data)
    file1.close()
    file2.close()


copy()


# f1 = open("../../day03/timg.jpeg", "rb")
# f2 = open("../../day03/mm.jpg", "wb")
# while True:
#     date1 = f1.read(1024)
#     if not date1:
#         break
#     f2.write(date1)
# f1.close()
# f2.close()
