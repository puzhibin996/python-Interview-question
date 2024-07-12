# python中常见的数据结构有：
# 1. ————————————————————————————————字典————————————————————————————————
# 创建字典


my_dict = {'name': 'zhangsan', 'age': 14}

# 使用构造函数 dict 创建字典
my_dict1 = dict(name='liusi', age=12)

print(my_dict)
print(my_dict1)

# 通过键访问
print(my_dict1['age'])
print(my_dict1['name'])

# 如果不确定键是否存在，可以通过get（）方法，这样如果键不存在就不会抛出异常
print(my_dict.get('age'))
print(my_dict.get('name'))

# 修改字典
# 添加新的键值对
my_dict['性别'] = '妖怪'
print(my_dict)

# 更新现有键的值
my_dict['age'] = 18
print(my_dict)

# 删除键值对
del my_dict['性别']
print(my_dict)

# 字典方法
# keys（） 返回字典的所有键的列表视图
keys_list = list(my_dict.keys())
print("keys_list:", keys_list)

# values() 返回字典的所有值的列表视图
values_list = list(my_dict.values())
print("values_list:", values_list)

# items() 返回字典的键值对的列表视图
items_list = list(my_dict.items())
print("items_list:", items_list)

# clear() 清空字典
my_dict.clear()
print("清空字典：", my_dict)

# pop(key) 移除指定键并返回对应的值，如果键不存在，则抛出异常，除非提供默认值。
value = my_dict1.pop('age')
print("pop移除指定键并返回对应的值：", value)
print(my_dict1)

# update(other_dict) 将其他字典的内容合并到当前字典中
my_dict.update({'new_key': 'new_value'})
print("update内容合并到当前字典中：", my_dict)

# 迭代字典
# 迭代字典的键
my_dict2 = {'name': 'zhangsan', 'age': 14, 'sex': '男'}
for key in my_dict2:
    print("迭代键：", key)

# 迭代字典的值
for value in my_dict2.values():
    print("迭代值：", value)

# 迭代字典的键值对
for key, value in my_dict2.items():
    print(f"键：{key}--值：{value}")

# 字典推导式
new_dict = {k: v * 2 for k, v in my_dict2.items()} # 推导式是值的倍数
print("字典推导式：", new_dict)

# 复制字典
new_copy_dict = my_dict2.copy()
print("复制字典：", new_copy_dict)

# 使用字典的字面量语法来创建嵌套字典
nested_dict = {'outer_key':{'inner_key':'inner_value'}, '性别':{'人':'男', '动物':'狗', '植物':'树'}}
print("嵌套字典：", nested_dict)

# 字典的嵌套列表
nested_list_dict = {'outer_key':[1, 2, 3], '性别':['男', '女']}
print("字典的嵌套列表：", nested_list_dict)

# 迭代嵌套字典
for key,value in nested_dict.items():
    print(f"键：{key} 值：{value}")


# 总结：
# 字典是python中最常用的数据结构之一，
# 因为他们提供了高效的查找和更新数据的能力，
# 尤其是在处理大量的数据和负载的数据结构是
# 字典是一个无需的键值对结合，使用{} 来定义的
# 键和值使用冒号 ： 分割
# 键必须是唯一的且不可变的（如字符串，数字或元组）
# 
