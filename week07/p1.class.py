class MyClass:
    pass

a = MyClass()
b = MyClass()

a.__class__()
b.__class__()

c = MyClass

d = c()
d.__class__()

dir(d)