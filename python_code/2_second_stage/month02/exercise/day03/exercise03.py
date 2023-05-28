"""
练习3： 查单词，编写一个程序，input输入一个单词，获取单词解释

     温馨提示： 每个单词占一行
              单词和解释之间一定有空格
              单词按照顺序排列 (后面单词比前面的大)
"""


def get_explain(word_name):
    file = open("dict.txt")
    flag = True
    for item in file:
        word = item.split()[0]
        if word_name == word:
            flag = False
            target = item[len(word) + 1:].strip()
            print(target)
    if flag:
        print("没有该单词。")
    file.close()


word_input = input(">> ")
get_explain(word_input)
