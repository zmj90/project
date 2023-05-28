"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(graphic)
        else:
            raise ValueError()

    def get_total_area(self):
        total_area = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__graphics:
            # 多态：
            # 调用的是图形
            # 执行的是圆形/矩形...
            total_area += item.calculate_area()
        return total_area

class Graphic:
    def calculate_area(self):
        # 如果子类不重写，则异常.
        raise NotImplementedError()
#-----------------------------------
class Circle(Graphic):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius **2


class Rectanlge(Graphic):
    def __init__(self,length,width):
        self.lenght = length
        self.width = width


    def calculate_area(self):
        return self.lenght *  self.width


c01 = Circle(5)
r01 = Rectanlge(10,20)
manager = GraphicManager()
manager.add_graphic(c01)
manager.add_graphic(r01)
re = manager.get_total_area()
print(re)