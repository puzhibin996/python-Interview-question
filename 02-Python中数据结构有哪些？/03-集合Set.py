# python中常见的数据结构有：
# 1. ————————————————————————————————集合————————————————————————————————
#
# 创建一个集合
set1 = {1, 3, 4, 5, 67, 1234, 1123, 23, 232, 334, 34, 434, 34, 343, 43, 4343, 3434343, 3435, 88, 99, 0, 123, 22, 12, 34}
print(set1)

# 获取集合的长度
a = len(set1)
print(a)

# 添加元素
set1.add('puzhibin')
print(set1)

# 删除元素
set1.remove('puzhibin')
print(set1)


# 遍历出大于100的元素
for i in set1:
    if i > 100:
        print(i)

# 将集合中的元素从小到大排序
set2=sorted(set1) # 这里将集合 转换为列表
print(set2)

# 将集合转换的列表元素从大到小排序
set2.reverse()
print(set2)

# 集合的交集 交集解释：集合A和集合B的交集就是集合A和集合B同时存在的元素，然后输出出来。
set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set4 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
set5 = set3 & set4 # 这里是集合运算符，不是集合方法
print("交集：",set5)

# 集合的并集 并集解释：集合A和集合B的并集就是集合A和集合B同时存在的元素，然后输出出来。
set33 = {1,2,3,4,5}
set44 = {4,5,6,7,8}
BJ = set33.union(set44) # 并集  去除重复元素
print("并集：",BJ)

# 交集： 同事出现的两个集合中的原
JJ = set33.intersection(set44) # 交集 包含两个集合共有的元素
print("交集：",JJ)


# 差集 ：在第一个集合中但不在第二个集合中的元素
CJ = set33.difference(set44) # 差集 包含在第一个集合中但不在第二个集合中的元素
print("差集：",CJ)

# 对称差集： 只要在一个集合中出现的元素
DCCJ = set33.symmetric_difference(set44)
print("对称差集：",DCCJ)

set5 = {1,2,3,4,5,6,7,8,9}
set6 = {3,4,5,6}

# 检查子集 判断一个集合是否是另一个集合的子集
zj = set6.issubset(set5)
print("子集：",zj)

# 检查超集 判断一个集合是否是另一个集合的超集
cj = set5.issuperset(set6)
print("超集：",cj)

# 集合支持 in-place操作，可以修改原有的集合
set33 |= set44
print("in-place |:",set33)

set33 &= set44
print("in-place &:",set33)

set33 -= set44
print("in-place -:",set33)

set33 ^= set44
print("in-place ^:",set33)


#总结：
# 集合是一个无需的不重复元素集合，使用大括号{}定义
# 支持集合运算、如并集、交集、、差集、对称差集
# union 是并集
# intersection 是交集
# difference 是差集
# symmetric_difference 是对称差集
# issubset 是子集
# issuperset 是超集
