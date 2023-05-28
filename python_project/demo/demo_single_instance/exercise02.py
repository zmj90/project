class Person:
    _instance = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_singleton(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    a = Person.get_singleton("python", 12)
    print(a.__dict__)
    b = Person.get_singleton("java", 13)
    print(b.__dict__)
    print(id(a), type(a), a)
    print(id(b), type(b), b)
