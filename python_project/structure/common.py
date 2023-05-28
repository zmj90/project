"""wendang字符串"""
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__']

# annotations = __annotations__

builtins = __builtins__
print(builtins, type(builtins))
# <module 'builtins' (built-in)> <class 'module'>

# cached = __cached__

doc = __doc__
print(doc, type(doc))
# wendang字符串 <class 'str'>

file = __file__
print(file, type(file))
# D:\doing\study\demo\python_project\structure\common.py <class 'str'>

# loader = __loader__

name = __name__
print(name, type(name))
# 当前模块运行
# __main__ <class 'str'>
# 非当前模块运行
# common <class 'str'>

package = __package__
print(package, type(package))

# spec = __spec__
