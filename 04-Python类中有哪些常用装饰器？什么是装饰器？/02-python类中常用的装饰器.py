# 在python类中，有一个常用的装饰器
# 1 @property
# 将一个方法转换为属性，这样你就可以像访问属性一样访问这个方法。

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


obj = MyClass(10)
print(obj.value)  # 调用getter

obj.value = 20  # 调用setter
print(obj.value)


# @staticmethod
# 将一个方法定义为静态方法，静态方法不需要类实例作为参数，可以通过类本身来调用。
class MyClass01:
    @staticmethod
    def static_method():
        print("This is a static method.")


MyClass01.static_method()


# @classmethod
# 将一个方法定义为类方法，类方法的第一个参数是类本身(通常命名为cls)，可以通过类或实例来调用。
class MyClass02:
    @classmethod
    def class_method(cls):
        print("This is a class method.")


MyClass02.class_method()


# 自定义类装饰器
# 你还可以在类中定义和使用自定义装饰器，例如，一个记录方法调用次数的装饰器
def count_calls(method):
    def wrapper(self, *args, **kwargs):
        self.calls += 1
        print(f"call{self.calls} of {method.__name__}")
        return method(self, *args, **kwargs)

    return wrapper


class MyClass03:
    def __init__(self):
        self.calls = 0

    @count_calls
    def say_puzhibin(self):
        print("puzhibin")


pzb = MyClass03()
pzb.say_puzhibin()
pzb.say_puzhibin()

# 总结
# 装饰器在python中是一中强大的工具，广泛用于函数和方法的行为修改，常见的类装饰器包括@property、@staticmethod和@classmethod。
# 他们提供了简洁且清晰的方式来定义属性，静态方法和类方法，通过自定义装饰器，你可以根据需求扩展类的方法功能，从而提高代码的可维护性和可读性。
