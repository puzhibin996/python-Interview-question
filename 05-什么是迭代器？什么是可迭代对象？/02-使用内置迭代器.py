


# python中许多内置对象都是迭代器，例如列表、元祖、字典、集合等
#使用内置迭代器
my_list = [1,2,3,4,5,6]
my_iter = iter(my_list)

while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break

# 总结：
# 迭代器：是一种对象，它实现 __iter__() 和 __next__()方法，使其能够逐一返回容器中的元素。
# 使用场景： 迭代器用于需要一次性大量访问数据的情况，例如读取文件内容，遍历数据集合等。
#           他们提供了以中国惰性计算（lazy evaluation）的方式，可以节省内存。
