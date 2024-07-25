







# lambda函数是python中一种简洁的、用于创建匿名函数的方法。匿名函数是指没有名称的函数，通常用于临时性定义一个小功能或处理简单的操作。
# 定义lambda函数
# lambda函数基本语法如下：

# lambda arguments：expression

# 这里 arguments是函数的参数化列表，expression是一个表达式，该表达式的结果就是函数的结果。
# 定义一个lambda函数，用于计算两个数的和
add = lambda x,y:x+y
# 调用lambda函数
result = add(5,3)
print(result)

# lambda 函数的好处
# lambda函数在python中有以下几个好处：
# 1.简洁性：lambda函数提供了一种快速定义小型功能的方法，不需要编写完整的函数定义。
# 2.内联使用：由于lambda函数式匿名的，他们通常在需要的地方直接定义和使用，这使得底阿妈更加紧凑和易于阅读
# 3.函数式编程：lambda函数式函数式编程的核心概念之一，他们使得python支持函数式编程范式。
# 4.高阶函数：lambda函数可以作为参数传递给高阶函数（如map（）、filter（），sorted（）等），这些函数接受一个函数作为参数，并应用该函数来处理数据。
# 使用场景：
# lambda函数在以下场景中特别有用
# 1.数据处理：在处理数据时，使用lambda函数可以快速定义简单的转换或过滤逻辑。
# 2.排序和比较：在对列表或集合进行排序时，lambda函数可以作为比较函数。
# 3.函数式编程：在函数式编程中，lambda函数可以用于创建简洁的函数组合

# 使用lambda函数filter（）函数过滤列表中的偶数
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(lambda x:x%2 == 0,numbers)
list_even_number = list(even_number)
print(list_even_number)

# 使用lambda函数和sorted（）函数对字典按值排序。
dict_data = {'apple':3,'banana':2,'orange':5}
# 从小到大排序
sorted_data_max = sorted(dict_data.items(),key=lambda item:item[1])
# 从大到小排序
sorted_data_min = sorted(dict_data.items(),key=lambda item:item[1],reverse=True)
print(sorted_data_max)
print(sorted_data_min)

# 注意事项
# 虽然lambda函数很简洁，但他们也有一些限制：
# lambda函数只能包含一个表达式，不能包含语句或多个表达式
# lambda函数不适合定义复杂的逻辑，应该用于简单的操作。

