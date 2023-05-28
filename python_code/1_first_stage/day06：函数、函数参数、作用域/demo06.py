"""
默认形参值会在执行函数定义时按从左至右的顺序被求值。 这意味着当函数被定义时将对表达式求值一次，
相同的“预计算”值将在每次调用时被使用。
"""


def fun1(a=0 or print("形参")):
    ...


def fun2(a=input("形参>>>")):
    ...


def fun3(a=input("形参>>>"), /, *args, b=1, c, **kwargs):
    ...


def fun4(a, /, d, *args, b=1, c, **kwargs):
    Ellipsis
