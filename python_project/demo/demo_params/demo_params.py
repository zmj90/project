def fun1(a=1, b=2, *, c, **kwargs):
    print(a, b, c)


if __name__ == '__main__':
    fun1(a=2, b=3, c=4)
