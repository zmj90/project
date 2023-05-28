"""
with语句块
"""

with open('file','r+') as f:  # f = open(xxxxx)
    data = f.read()
    print(data)
    f.write("xxxxxxxx")

# with结束后f 自动销毁