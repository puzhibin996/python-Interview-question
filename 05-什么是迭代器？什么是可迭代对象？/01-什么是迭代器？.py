


# 在python中，迭代器是实现了迭代协议的对象。迭代协议包含两个核心方法。

# __iter__() 和 __next__()。这些方法使得对象能够被逐一访问，直到所有元素都被访问完毕。

# 迭代器的基本概念
# __iter__() 方法返回迭代器对象本身，它允许对象被迭代。
# __next__() 方法返回容器的下一个元素。如果没有更多的元素，则抛出StopIteration异常。

# 自定义一个简单的迭代器
class MyIterator:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
# 创建一个MyIterator对象
my_iter = MyIterator([1,2,3,4,5,6])
# 使用迭代器
for i in my_iter:
    print(i)

# 语义解释：
# 创建迭代器对象
# my_iter = MyIterator([1,2,3,4,5,6]) 创建一个MYIterator对象，初始化数据和索引
# 实现__iter__()方法
#   __iter__()方法返回迭代器对象本身，这使得对象可以被用于迭代。
# 实现__next__()方法
#   __next__() 方法用于返回下一个元素。在每次调用时，他检查当前索引是否小于数据长度。如果是，则返回当前索引对应的数据。
#   并将素银加一。如果索引超出数据长度，则抛出StopIteration异常，表示迭代结束。
