"""
编写一个函数，实现文件的打印。函数参数为一个文件名，运行函数会打印这个
文件的内容，打印的内容要跟文件一样，并且文件可能比较大不允许一次性读取。
"""


# def get_print(file_name):
#     file = open(file_name)
#     for i in file:
#         print(i, end="")
#     print()
#     file.close()


# def get_print(file_name):
#     file = open(file_name)
#     while True:
#         date = file.read(1024)
#         if not date:
#             break
#         print(date, end='')
#         file.close()


def get_print(file_name):
    file = open(file_name)
    while True:
        data = file.readline()
        if not data:
            break
        print(data, end="")
    print()


get_print("text.txt")
