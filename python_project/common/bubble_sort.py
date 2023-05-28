"""
冒泡排序

"""


def bubble_sort(int_list):
    for i in range(len(int_list) - 1):
        flag = True
        for j in range(len(int_list) - 1 - i):
            if int_list[j] > int_list[j + 1]:
                flag = False
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
        if flag:
            break
