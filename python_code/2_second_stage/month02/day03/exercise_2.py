"""
编写一个函数，实现文件的打印。函数参数为一个文件名，运行函数会打印这个
文件的内容，打印的内容要跟文件一样，并且文件可能比较大不允许一次性读取。
"""

def cat(filename):
    try:
        f = open(filename) # 默认以读方式打开
    except Exception:
        print("cat: %s: 没有那个文件或目录"%filename)
    else:
        while True:
            data = f.read(1024)
            if not data:
                break
            print(data,end='')
        f.close()

filename = input(">>") # 输入一个文件名字
cat(filename) # 讲文件名字传给函数参数
