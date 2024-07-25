from abc import ABC,abstractmethod





# 在面向对象编程中，抽象类是一种不能被实例化的类，他主要用来定义一些通用的行为和接口，并且强制子类去实现这些行为。
# 抽象类通过包含一个或多个抽象方法，这些方法没有具体的实现，只有子类才能给出具体实现。
## 如何定义抽象类
# 在python中，可以通过abc模块（Abstract Base Classes）来定义抽象基类。下面是一个例子：


class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass
    # 这个方法不是抽象方法，所以可以有默认的实现
    def another_method(self):
        print("This is not an abstract method")
    #这个方法没有@abstractmethod装饰器，所以不是抽象方法
    def yet_another_method(self):
        raise NotImplementedError("Subclasses should implement this!")
# 由于AbstractClassExample包含抽象方法，所以不能直接实例化。

class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().another_method()
        print("the subclass is doing something! ")

# 创建一个子类实例。
my_object = AnotherSubclass()
my_object.do_something()

# 在上面代码中，AbstractClassExample是一个抽象基类，它包含了一个抽象方法do_something和两个非抽象方法another_method和yet_another_method。
# AnotherSubclass继承了AbstractClassExample并实现了抽象方法do_sometiong
