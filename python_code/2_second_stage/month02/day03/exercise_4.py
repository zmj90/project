"""
重点代码
练习4： 文件的拷贝
       有一个文件  timg.jpeg,将其拷贝一份到主目录下，命名为 mm.jpg

       从源文件读取，写入到目标文件

思路 ： 从timg.jpeg中读取内容，原样写入到mm.jpg
"""

fr = open('timg.jpeg','rb')  # 源文件
fw = open('/home/tarena/mm.jpg','wb') # 新文件

while True:
    data = fr.read(1024)
    # 读到文件结尾返回空字符串
    if not data:
        break
    fw.write(data)

fr.close()
fw.close()
