import math

# map（） 可以与更复杂的函数一起使用，例如与标准库中的函数结合，或者自定义函数。
# 下面的例子展示了如何使用math.sqrt 函数计算列表中所有平方根。

numbers = [4,9,16,25]
# 使用map（） 和math.sqrt 函数计算列表中所有平方根。
square_roots = map(math.sqrt, numbers)

square_roots_list = list(square_roots)
print(square_roots_list)

# map（）函数是python中处理数据流和进行函数式编程的重要工具之一，它能够高效地对数据库进行转换和操作。