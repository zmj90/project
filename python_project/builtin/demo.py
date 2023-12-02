def f1(n):
    # return sum([2 * i - 1 for i in range(1, n + 1)])
    return sum((2 * i - 1 for i in range(1, n + 1)))


def f2(n):
    return (1 + 2 * n - 1) * n / 2


if __name__ == '__main__':
    print(f1(10))
    print(f2(10))
