class MyProperty:
    def __init__(self, name):
        print(f'name = {name}')
        self.name = name.upper()

    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')
        # return super().__get__(instance, owner)
        return self.name

    def __set__(self, instance, value):
        # return super().__set__(instance, value)
        print('setter is  called')
        self.name = value
    
    def __delete__(self, instance):
        print(f'__delete__{instance}')
        del self.name


class Person:
    name = MyProperty('zhangsan')
    # def __init__(self):
    #     self.name = 
    
    def intruduce(self):
        print(self.name)

me = Person()
me.name

