"""
    课程二：
         设计思想：详见面向对象答辩
         语法：类和对象

"""
# 面向过程的老婆
# wife.py
name = "双儿"
age = 22


# 现实世界  -抽象化-> 类(模板) -实例化->  对象
# 面向对象的老婆
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# 一个类型(行为相同)的多个对象(数据不同).
w01 = Wife("双儿", 22)
w02 = Wife("苏荃", 32)
# 通过对象访问实例成员
print(w01.name)


# 类变量(一份数据)
# 此时相当于面向过程
class Wife02:
    name = name
    age = age


# 通过类名访问类成员
print(Wife02.name)


class Wife03:
    sex = "女"

    def __init__(self, name):
        self.name = name

    # 实例方法:操作实例变量
    def print_name(self):
        print("我的名字是", self.name)

    # 类方法
    @classmethod
    def print_sex(cls):
        print("我们的性别都是：", cls.sex)

    # 静态方法
    @staticmethod
    def tool():
        print("独立与类的工具")


w03 = Wife03("双儿")
# 通过对象调用实例方法
w03.print_name()
# 通过类调用类方法
Wife03.print_sex()
# 通过类调用静态方法
Wife03.tool()


class Singleton:
    __instance = None

    # 单例模式：保障当前类创建的对象只能有1个
    def __new__(self, *args, **kwargs):
        # if Singleton.__instance:
        #     return self
        # else:
        #     Singleton.__init__(self, *args, **kwargs)
        #     return self
        if Singleton.__instance == None:
            Singleton.__init__(self, *args, **kwargs)
        return self

    def __init__(self, data):
        self.data = data
        Singleton.__instance = self


# 先执行__new__ 再执行__init__
s04 = Singleton(data="双儿")
s05 = Singleton(data="苏荃")
print(s04.data)
print(s05.data)
