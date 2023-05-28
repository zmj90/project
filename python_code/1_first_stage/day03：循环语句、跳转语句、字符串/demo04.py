"""
    str字面值
    转义符：改变原始字符含义的特殊符号
"""
name = "苏大强"
# 可见即所得
name = '''苏大强'''
name = """
         苏
        大
        强
"""
print(name)

# 单引号内的双引号不算结束符
message = '我叫"苏大强"。'
# 双引号内的单引号不算结束符
message = "我叫'苏大强'。"

# 转义符：\"　\n  \t  \\
message = "我叫\"苏大强\"。"
message = "我叫\n苏大强。"  # 换行
message = "我叫\t苏大强。"  # 水平制表格ｔａｂ键

url = "C:\\nltk_data\\aodels\\bmt15_eval"
# 原始字符串(没有转义符)
url = r"C:\nltk_data\aodels\bmt15_eval"
print(url)
