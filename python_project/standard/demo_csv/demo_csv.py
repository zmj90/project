"""
https://docs.python.org/zh-cn/3/library/csv.html
"""

import csv


def fun1():
    with open('eggs.csv', newline='') as csv_file:
        # spam_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='&')
        for row in spam_reader:
            print(', '.join(row))
            print(row)


def fun2():
    with open('eggs1.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked| Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


if __name__ == '__main__':
    fun2()
