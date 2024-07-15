


# 可迭代对象
# 实现了__iter__() 方法，范湖一个迭代器对象
# 例如：列表、元祖、集合、字典、字符串等。
# 列表是可迭代对象
my_list = [1,23,3,4,5]
for i in my_list:
    print(i)

my_key_value = {'name':'zhangsan','age':19}
for key,value in my_key_value.items():
    print(key,value)

# 使用内置迭代器
my_key_value1 = {'name':'zhangsan','age':22}
my_tier = iter(my_key_value1)
for key,value in my_key_value1.items():
    print(key,value)



# 可迭代对象：实现了__iter__() 方法返回一个迭代器对象，可以被迭代。