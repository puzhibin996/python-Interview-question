import operator
# reduce（） 函数是functools模块中的一个函数，他对可迭代对象中的元素执行累积操作。
# 与map（）和filter（）不同，reduce（）不包含在python的内置函数中，因此你必须从functools模块导入它才能使用

# reduce（） 函数的基本语法如下：

from functools import reduce

# 定义一个数字列表
numbers = [5,2,9,1,5,6,3]
# 使用reduce（）函数和map（）函数来找到列表中的最大值
max_number = reduce(max,numbers)
min_number = reduce(min,numbers)
print(min_number)
print(max_number)


# 计算列表中所有元素的和
# 这是reduce（） 最常见的用途之一，你可以使用reduce（）和lambda函数或者operator.add来计算列表中鄋的数值的总合

numbers1 = [1,2,3,4,5]
sum_of_numbers = reduce(operator.add,numbers1)
print(sum_of_numbers)
# 或者使用lambda函数
sum_of_numbers1 = reduce(lambda x,y:x+y,numbers1)
print(sum_of_numbers1)


# 计算列表中素有元素 乘积
# 类似地可以使用reduce（）来计算列表中所有数值的乘积
numbers2 = [1,2,3,4,5]
product_of_numbers = reduce(lambda x,y:x*y,numbers2)
print(product_of_numbers)

# 拼接字符串
# reduce（）可以用来拼接一个字符串列表。
words = ['puzhibin',' ','I Love You','zengting']
joined_string = reduce(lambda x,y:x+y,words)
print(joined_string)


# 连接嵌套列表