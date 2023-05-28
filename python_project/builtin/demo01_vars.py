class Book:
    def __init__(self):
        self.name = "sdf"
        self.city = "dsf"
        self.title = "电风扇"

    def d_r(self):
        print("sdfsdf")


if __name__ == '__main__':
    b = Book()
    r1 = b.__dict__
    print(r1, type(r1))
    r2 = vars(b)
    print(r2, type(r2))
