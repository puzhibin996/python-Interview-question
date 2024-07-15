


# 在python中生成器是一种特殊的迭代器，用于生成一些列值。生成器通过使用yield 关键字的函数定义。
# 与普通函数不同，生成器函数在每次调用yield时会暂停并保存其状态，下次恢复执行时从上次暂停的地方继续。


# 生成器的基本概念
# yield关键，：生成器函数使用yield关键字返回一个值，并暂停执行。下一次调用生成器的__next__()方法时，从暂停的笛梵继续执行。
# 生成器对象：调用生成器函数会返回一个生成器对象，该对象实现了迭代器协议，可以使用__iter_() 和 __next__()方法

#创建生成器函数
def my_generator():
    yield 1
    yield 2
    yield 3

# 创建生成器对象
gen = my_generator()
# 使用for循环遍历生成器对象
for value in gen:
    print("我是第一层for循环：",value)
    if value == 1:
        break

for value in gen:
    print("我是第二层for循环：",value)
    if value ==3:
        break

# 生成器工作机制
# 定义生成器函数
#   def my_generator(): 定义了一个生成器函数，它包含了三个yield表达式
# 创建生成器对象
#   gen = my_generator（）：调用生成器函数，返回一个生成器对象gen
# 迭代生成器对象
#   for value in gen： 使用for循环遍历生成器对象。每次循环调用生成器的__next__() 方法，从上次暂停的地方继续执行。并返回下一个值。


#   带状态的生成器对象
#   生成器可以保存内部状态，这使得他们非常适合用于生成一系列值，流入裴波那切数列
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b



# 创建生成器对象
fib = fibonacci(10)

# 使用for循环遍历生成器对象
for value in fib:
    print("我是fib：",value)


# 无限序列生成器
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

# 创建生成器对象
inf_seq = infinite_sequence()
# 获取前五个值
for _ in range(10):
    print("我是inf_seq：",next(inf_seq))



# yield 关键字
#   每次遇到yield表达式时，生成器函数会暂停执行，并返回yield后的值。生成器函数的状态会被保存（包括本地变量、指令指针等）
# 恢复执行：
#   下一次调用生成器对象的__next__()方法时，生成器函数从上次在哪提的地方继续执行，知道再次遇到yield表达式或结束。

# 总结
# 生成器：是一种特殊的迭代器，通过使用yield关键字的函数定义，生成器函数在每次调用yield时会暂停执行，并保存其状态。
# 生成器对象： 调用生成器函数返回一个生成器对象，该对象实现了迭代器协议，可以用于迭代操作。



