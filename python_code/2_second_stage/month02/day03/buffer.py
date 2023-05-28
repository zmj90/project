"""
缓冲区示例
"""

# f = open("file",'w') #　普通缓冲  常用

# f = open('file','w',1) # 行缓冲  换行自动刷新

f = open('file','wb',10) # 设置缓冲区为10字节

while True:
    data = input(">>")
    if not data:
        # 直接回车结束循环
        break
    f.write(data.encode())
    # f.flush()  #　手动刷新缓冲

f.close()