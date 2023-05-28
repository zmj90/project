"""
    变量
"""
# 创建单个变量
person_name01 = "吉多"
# 用多个数据，创建多个变量
person_name02, person_name03 = "范罗苏姆", "林纳斯"
# 用单个数据，创建多个变量
person_name04 = person_name05 = "托瓦兹"

del person_name04
del person_name01, person_name02

person_name06 = person_name05 + person_name05
