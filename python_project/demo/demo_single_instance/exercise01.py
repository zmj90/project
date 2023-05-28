from demo.demo_single_instance.singleton import instance

a = instance
b = instance
print(id(a), id(b))
