




#  python中 filter（） 函数是一个内置函数，用于根据某个函数的判断条件来筛选序列（如列表、元祖、集合等）中的元素。
#  filter（） 接受两个参数：一个是函数，另一个是可迭代对象。她会将可迭代对象中的每一个元素传递给函数，然后返回一个迭代器，
# 该迭代器质保函那些函数返回值为True的元素。

# 基本语法：
# filter（function，iterable）
#  function： 一个函数，他接受一个参数并返回布尔值。True False
#  iterable： 一个可迭代对象，如列表、元祖、集合等

# 返回值
# filter（） 函数返回的是一个迭代器，所以通常需要转换为列表、元组或其他容器类型才能查看结果。


# 示例：
# 假设我们有一个列表，我们想要过来出来所有的偶数

numbers = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数，检查一个数是否为偶数。
def is_even(n):
    return n % 2 == 0

# 使用filter（）函数过滤处偶数
even_numbers = filter(is_even,numbers)

# 奖结果转换为列表并打印
even_numbers_list = list(even_numbers)
print(even_numbers_list)


