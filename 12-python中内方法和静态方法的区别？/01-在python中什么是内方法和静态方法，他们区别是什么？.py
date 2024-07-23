








# 在python中 类的方法可以有几种不同的类型，主要分为实例方法、类方法、静态方法。每种方法的定义和使用场景都有所不同：
# 实例方法
# 实例方法需要通过类的实例来调用，并且默认接受self参数作为第一个采纳数，指向该方法被调用时的实例。实例方法可以访问和修改实例属性以及类属性。

class MyClass:
    def instance_method(self):
        print('this is an instance method')

obj = MyClass()
obj.instance_method()


# 类方法
# 类方法使用@classmethod装饰器定义，并且第一个采纳数通常命名为cls，代表类本身。类方法可以访问和修改类属性，但不能修改实例属性，因为他们不依赖于特定实例。

class MyClass01:
    class_var = "i m a class variable."
    @classmethod
    def class_method(cls):
        print(cls.class_var)
MyClass01.class_method()


# 静态方法
# 静态方法使用@staticmethod装饰器定义，它既不接受self也不接受cls作为惨所。静态方法不依赖于类的状态，可以看做是 与类关联的普通函数。
# 他们主要用于封住哪个与类相关的功能，但不需要访问实例或类状态。

class MyClass02:
    @staticmethod
    def static_method(a,b):
        return a+b
result = MyClass02.static_method(2,3)
print(result)

# 总结：
# 实例方法用于操作实例状态，类方法用于操作类状态，而静态方法则不涉及类或实例的状态，通常用于实现与类相关但不依赖于其状态的功能。选择那种方法类型取决于你的具体需求。

