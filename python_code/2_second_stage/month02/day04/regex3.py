"""
match对象使用
"""

import re

s = "abcdefghi"
pattern = "(ab)cd(?P<address>ef)"

obj = re.search(pattern, s)  # 获取match对象

print(obj.span())  # s[0:6] 获取匹配到的内容在目标字符串中的位置
print(type(obj.span()))  # s[0:6] 获取匹配到的内容在目标字符串中的位置
print(obj.groupdict())  # 获取捕获组字典 组名为键，匹配到的内容为值
print(obj.groups())  # 获取子组匹配到的内容
print(type(obj.groups()))  # 获取子组匹配到的内容
print(obj.group())  # 获取匹配内容
print(obj.group("address"))  # 获取匹配内容
print(obj.group(1))  # 获取匹配内容
print(obj.group(2))  # 获取匹配内容
