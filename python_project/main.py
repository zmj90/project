# from demo import demo02

s1 = '生\\n吞\\n'
s2 = s1.replace("\\t", "\n")
# print(s1)
# print(s2)


class Person:
    def __init__(self, name=None, title=None, tag=None):
        tag = tag
        self.name = name
        self.title = title

    def fun1(self):
        print("fun1")

    def fun2(self):
        return "fun2"


if __name__ == '__main__':
    r1 = Person().__dir__()
    print(r1)
