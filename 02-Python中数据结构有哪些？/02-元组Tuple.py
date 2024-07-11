# python中常见的数据结构有：
# 1. ————————————————————————————————元组————————————————————————————————
#————————————————————————————————创建元组集合
my_tuple = (1,2,3,444,52,121,1,34,5,6)
print(my_tuple)

# ————————————————————————————————元组索引
tuple1 = my_tuple[1]
print(tuple1)

# ————————————————————————————————元组切片
tuple2 = my_tuple[0:2] # 0:2表示从0开始，到2结束，不包含2
print(tuple2)

tuple3 = my_tuple[1:6] # 1:6表示从1开始，到6结束，不包含6
print(tuple3)

tuple4 = my_tuple[:] # 默认从0开始，到结束
print(tuple4)

# ————————————————————————————————切片洗
#对元组内容大于40的进行切片
for i in my_tuple:
    if i > 40:
        print(i)
        # 获取索引
        print(my_tuple.index(i))
        # 根据索引进行切片
        print(my_tuple[my_tuple.index(i):])


# 总结：元组是一个有序的集合，与列表类似，但是元组一旦创建了不能修改（即不可变），使用圆括号（） 来定义。
# 支持索引和切片操作
