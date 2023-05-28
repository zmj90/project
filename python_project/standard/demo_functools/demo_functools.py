from functools import cache, wraps


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


r1 = factorial(10)  # no previously cached result, makes 11 recursive calls
print(r1, f"{r1=}, {type(r1)=}")
# 3628800 r1=3628800, type(r1)=<class 'int'>
r2 = factorial(5)  # just looks up cached value result
print(r2, f"{r2=}, {type(r2)=}")
# 120 r2=120, type(r2)=<class 'int'>
r3 = factorial(12)  # makes two new recursive calls, the other 10 are cached
print(r3, f"{r3=}, {type(r3)=}")
# 479001600 r3=479001600, type(r3)=<class 'int'>


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


# >>> example()
# Calling decorated function
# Called example function
# >>> example.__name__
# 'example'
# >>> example.__doc__
# 'Docstring'
