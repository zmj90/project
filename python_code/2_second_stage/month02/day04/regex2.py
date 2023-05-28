"""
re模块示例，生成match对象

一个match对象对应一处匹配内容
用于获取匹配到内容的详细信息
"""

import re

s = "时，2020年春，AID 2002 班开课"
# s = "2020年春，AID 2002 班开课"

pattern = r"\d+"
# pattern = r"a"

# 匹配返回迭代器
it = re.finditer(pattern ,s)

for i in it:
    print(i.group())  # 得到match对象

# 匹配开头位置
# obj = re.match(pattern,s)
# print(obj.group())

# 匹配第一处
obj = re.search(pattern,s)
print(obj.group())

