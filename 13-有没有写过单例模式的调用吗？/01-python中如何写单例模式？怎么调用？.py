


# 单例模式是一种设计模式，用于确保一个类只有一个实例，并提供了一个全局访问点。
# 在python中，实现单例模式有多种方法。

# 使用__new__方法
# python中 __new__是一个特殊方法，用于控制对象的创建过程。我们可以通过重写__new__方法来确保类的实例只被创建一次

class Singleton:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

# 调用单例类
singleton1 = Singleton()
singleton2 = Singleton()

# 验证是否为同一实例
print(singleton1 is singleton2)

# 在这个例子中，每次调用Singleton（）构造函数时，都会检测_instance是否已经存在。如果_instance 还没有被创建，就会去创建一个新的实例。
#  如果_instance 已经存在，就直接返回这个已存在的实例。


# 使用装饰器
# 另一个实现单例模式的方式是使用装饰器。这种方式更加灵活，可以应用于任何类。
def singleton(cls):
    instances = {}
    def get_instance(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return get_instance
@singleton
class MyClass:
    pass
# 调用装饰器 单例模式
my_instance1 = MyClass()
my_instance2 = MyClass()
# 议案正是否为同一实例
print(my_instance1 is my_instance2)
# 这里 singleton 装饰器负责管理所有被装饰类的实例。当第一次调用MyClass（）时，singleton装饰器会创建一个实例并保存在instances字典中。之后的所有调用都将返回这个唯一的实例。
#
