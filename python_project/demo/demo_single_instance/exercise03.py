def singleton(cls):
    _instance_dict = {}  # 采用字典，可以装饰多个类，控制多个类实现单例模式

    def inner(*args, **kwargs):
        if cls not in _instance_dict:
            _instance_dict[cls] = cls(*args, **kwargs)
        return _instance_dict.get(cls)

    return inner


@singleton
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    stu1 = Student('jack', 18)
    stu2 = Student('jack', 1)
    print(stu1 is stu2)
    print(stu1.__dict__, stu2.__dict__)
