class SingleTon:
    _instance_dict = {}

    def __init__(self, cls_name):
        self.cls_name = cls_name

    def __call__(self, *args, **kwargs):
        if self.cls_name not in SingleTon._instance_dict:
            SingleTon._instance_dict[self.cls_name] = self.cls_name(*args, **kwargs)
        return SingleTon._instance_dict.get(self.cls_name)


@SingleTon  # 这个语法糖相当于Student = SingleTon(Student),即Student是SingleTon的实例对象
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    stu1 = Student('jack', 18)
    stu2 = Student('jack', 18)
    print(stu1 is stu2)
    print(stu1.__dict__, stu2.__dict__)

# 原理：在函数装饰器的思路上，将装饰器封装成类。
# 程序执行到与语法糖时，会实例化一个Student对象，这个对象是SingleTon的对象。
# 后面使用的Student本质上使用的是SingleTon的对象。
# 所以使用Student('jack', 18)来实例化对象，其实是在调用SingleTon的对象，会触发其__call__的执行
# 所以就在__call__中，判断Student类有没有实例对象了。
