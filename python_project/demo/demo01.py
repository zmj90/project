"""
f(n) = f(n-1) + f(n-2)
"""


def fun1(n):
    if n in (1, 2):
        return 1
    return fun1(n-1) + fun1(n-2)


if __name__ == '__main__':
    r = fun1(9)
    print(r)
