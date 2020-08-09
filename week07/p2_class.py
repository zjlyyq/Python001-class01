class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name

man = Human('Adam')
woman = Human('Eve')

# 有静态字段,live属性
print(Human.__dict__)
# 有普通字段,name属性
print(man.__dict__)

# 实例可以使用普通字段也可以使用静态字段
man.name
man.live = False
# 查看实例属性
man.__dict__ #普通字段有live变量
man.live
woman.live

# 类可以使用静态字段
Human.live
woman.live = False
woman.live
woman.__dict__

# 可以为类添加静态字段
Human.newattr = 1
dir(Human)
dir(woman)
# woman.__dir__()
Human.__dict__

# 内置类型不能增加属性和方法
setattr(list, 'newattr', 'value')
# TypeError
# 可以使用这种方法增加属性和方法
setattr(Human, 'age', 20)
me = Human('zhang san')
dir(Human)
dir(me)
me.age

# 显示object类的所有子类
print( ().__class__.__bases__[0].__subclasses__() )

