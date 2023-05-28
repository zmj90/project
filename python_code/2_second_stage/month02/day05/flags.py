"""
正则表达式功能扩展
"""

import re

# 目标字符串
s = """Hello 
北京"""

# 只能匹配英文
l = re.findall(r"\w+",s,flags=re.A)
print(l)

# .可以匹配换行
l = re.findall(r".+",s,flags=re.S)
print(l)

# 匹配时不区分字母大小写
l = re.findall(r"[a-z]+",s,flags=re.I|re.A)  # 多个功能扩展
print(l)

# ^和$能表示每行开头结尾位置
l = re.findall(r"^北京",s,flags=re.M)
print(l)