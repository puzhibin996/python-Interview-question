







# 通常，为了简化代码，我们可以使用匿名函数（lambda表达式） 来代替定义一个单独的函数

numbers = [1,2,3,4,5,6,7,8,9,10]

# 使用lambda 表达式filter（）函数过滤处偶数
even_numbers = filter(lambda n: n%2 ==0,numbers)

even_numbers_list = list(even_numbers)
print(even_numbers_list)

