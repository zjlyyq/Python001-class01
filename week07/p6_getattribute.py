class Amimal:
    def __init__(self, age):
        super().__init__()
        self.age = age
    
    # 拦截已定义的属性的读取动作
    def __getattribute__(self, name):
        print('__getattribute__')
        # return "my age is " + self.age
        return "my age is " + str(super().__getattribute__(name))
    
    # 拦截未定义的属性的读取动作
    def __getattr__(self, name):
        print('__getattr__')
        return "ok"


cat = Amimal(10)
print(cat.age)  # my age is 10
print(cat.name) # ok
