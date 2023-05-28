class Student:
    _instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':
    stu1 = Student('jack', 18)
    stu2 = Student('jack', 12)
    print(stu1 is stu2)
    print(stu1.__dict__, stu2.__dict__)
