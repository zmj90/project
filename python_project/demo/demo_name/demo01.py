_ = 1
_l = [1]
_l_ = (1,)
_l__ = (1, 2)
__l__ = {1, 2}
l1 = [2]


def _fun1():
                pass


def __fun1():
    pass


def fun1():
    pass


class Fun1:
    _ = 3
    _L = [3, ]
    __L = (3,)
    __L_ = {3, }
    __L___ = {3, 4}

    def __m1(self):
        ...

    def _m1(self):
        ...

    def m1(self):
        ...
