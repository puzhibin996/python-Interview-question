import copy

# 在python中，对象的复制可以通过浅拷贝shallow copy 和深拷贝deep copy两种方式进行。
# 这两种拷贝方法在处理复杂数据结构时（如列表或字典包含其它可变对象）的行为有所不同

# 浅拷贝 shallow copy
# 浅拷贝会创建一个新对象，这个新对象具有原始对象中所有元素的引用。这意味着对于不可变类型（如整数、字符串、元组等），
# 浅拷贝会创建这些值的新副本；但对于可变类型（如列表、字典等），浅拷贝会直接引用原始对象。
# 如果原始对象中某个元素被修改，那么浅拷贝得到的对象中的元素也会被改变。

original_list = [[1,2],[3,4]]
shallow_copy_list = copy.copy(original_list)

original_list[0][0] = 'a'
print(original_list)
print(shallow_copy_list)

# 深拷贝 deep copy
# 深拷贝则会递归地负责整个数据结构，包括所有嵌套的对象，这意味着对原始对象的任何修改都不会影响到深拷贝得到的对象。每个对象都会被独立复制，即使他们是可变的。

original_list1 = [[1,2],[3,4]]
deep_copide_list = copy.deepcopy(original_list1)

original_list1[0][0]='puzhibin'
print(original_list1)
print(deep_copide_list)

# 总结来说，浅拷贝仅复制了最外层的容器，而深拷贝会复制所有层次上的对象，确保得到完全独立的副本。
# 在处理复杂的、嵌套的数据结构时，深拷贝通常能够提供更安全的操作环境。

