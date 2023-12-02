class Abs:
    def __abs__(self):
        return "自定义abs"


r1 = abs(-12.23)
print(r1, type(r1))
r2 = abs(12)
print(r2, type(r2))
r3 = abs(Abs())
print(r3, type(r3))
