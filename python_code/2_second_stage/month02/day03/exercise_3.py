"""
练习3： 查单词，编写一个程序，input输入一个单词，获取单词解释

     温馨提示： 每个单词占一行
              单词和解释之间一定有空格
              单词按照顺序排列 (后面单词比前面的大)
"""


def find_word(word):
    # 读文本打开文件
    f = open("dict.txt")
    for line in f:
        w = line.split(' ')[0]
        # 如果查找到的单词已经比目标大了，就没必要继续了
        if w > word:
            print("没有该单词")
            break
        if w == word:
            # 找到单词
            print(line)
            break
    else:
        print("没有该单词")

    f.close()


word = input("Word:")
find_word(word)

