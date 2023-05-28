"""

"""


class Person:
    p_v = "类变量"

    def __init__(self, name):
        self.name = name

    @classmethod
    def c_method(cls):
        print(f"{cls.p_v}: 类方法")

    @staticmethod
    def s_method():
        print("静态方法")

    def instance_method(self):
        print(f"{self.name}: 实例方法")


if __name__ == '__main__':
    r1 = dir(Person)
    # print(r1)
    r2 = hasattr(Person, "instance_method")
    # print(r2)
    r3 = getattr(Person("a"), "instance_method")
    r3()
