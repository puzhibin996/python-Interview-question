


# map（） 可以同时处理多个可迭代对象，例如，如果我们有两个列表，并希望将它们相加
list1 = [1,2,3]
list2 = [4,5,6]

# 使用map（）和lambda表达式将两个列表中的元素相加
summed = map(lambda x,y:x+y,list1,list2)

summed_list = list(summed)
print(summed_list)

# map() 返回的是一个迭代器，意味着结果只能遍历一次。如果你需要多次使用结果，记得先将其转换为列表或其他容器类型。
# 如果提供的可迭代对象长度不同，map() 函数会在最短的可迭代对象结束后停止。