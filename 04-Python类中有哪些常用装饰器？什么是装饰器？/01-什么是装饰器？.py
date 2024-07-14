



# 在python中装饰器是一种特殊类型的函数，用于在不修改原有的函数代码情况下增强或修改函数的功能。
# 装饰器接收一个函数作为参数，并返回一个新的函数，这个新函数通常会添加额外的行为或功能。
# 装饰器本质上是一个高阶函数，即接收函数作为参数并返回函数的函数。

# 装饰器的基本语法如下：

# 装饰器是一种用于修改函数或方法行为的高阶函数。它允许在不改变函数本身代码的情况下，动态增强功能。
# 装饰器通常用 @decorator_name 的语法放在被装饰函数定义的前一行。
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# 在上面的列子中，my_decorator是一个装饰器，他在被调用func之前和之后添加了一些额外的行为。



