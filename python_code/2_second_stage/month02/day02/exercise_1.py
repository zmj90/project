"""
编写一个函数，参数传入一个任意的英文字符串。字符串中单词之间有一个空格，函数的返回值
      是这个字符串的单词个数。
         提示 ： 字符串的 split() 方法
"""

def get_words_num(s=''):
    l = s.split(' ') # 按照空格切割字符串
    return len(l)

print(get_words_num("I love China"))