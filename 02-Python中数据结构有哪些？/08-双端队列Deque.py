# python中常见的数据结构有：
# 1. ————————————————————————————————双端队列————————————————————————————————
from collections import deque

# python的标准库collections模块提供了deque类来实现双端队列，
# 创建双端队列
d = deque() # 创建一个空的双端队列
d = deque(['a','b','c']) #创建一个初始化的双端队列
print(d)


# 双端队列的基本操作
# 在右边插入元素 append
d.append('puzhibin')
print("从右插入元素：",d)

# 在左边插入元素 appendleft
d.appendleft('zengting')
print("从左插入元素：",d)

# 从右边移除元素 pop
del_pop = d.pop()
print("从右移除元素：",del_pop)

# 从左边移除元素 popleft
del_pop_l = d.popleft()
print("从左移除元素：",del_pop_l)

# 检查双端队列是否为空
empty = deque()
if not empty:
    print("deque 为空")

# 获取双端队列的长度
length = len(d)
print("双端队列的长度：",length)


# 迭代双端队列
for item in d:
    print(item)


# 双端队列的高级操作
# 旋转双端队列
pp = deque(['1','2','3','4'])
pp.rotate(1)# 想右旋转1次
print("向右旋转后：",pp)

pp.rotate(-1)
print("向左旋转后：",pp)


# 扩展双端队列
pp.extend(['e','for '])# 在右添加多个元素
print("在右扩展双端队列：",pp)

pp.extendleft(['x','y'])# 在左边添加多个元素，注意元素的顺序会被反转
print("在左扩展双端队列：",pp)


# 总结
# 双端队列是一种线性数据结构，允许在其两端进行插入和删除操作，这种灵活性使得双端队列在多种应用场景中非常有用，
# 既可以像队列那样支持先进先出FIFO操作，也可以像栈那样支持后进献出LIFO操作。
# 双端队列的应用场景
# 滑动窗口算法： 在处理数据流时，双端队列可以用来维护一个固定大小的窗口，用于计算滑动窗口内的统计数据。
# 最近最少使用LRU缓存： 双端队列可以用来实现高效的LRU缓存策略，最近使用的元素放置在队列的一端，而最少使用的元素放到另一端。
# 多任务调度： 在多任务环境或事件驱动的程序中，双端队列可以采用调度任务，根据任务的优先级或达到顺序进行处理。
# 数据缓冲： 双端队列可以作为数据缓存区，既可以从一断接受数据，也可以从另一端发送数据。
# 字符串或数据的反转： 双端队列可以很容易地反转数据或字符串，只需从一端添加数据，然后从另一端读取即可。
# 算法中的栈和队列操作： 双端队列可以同时模拟栈和队列的行为，提供灵活的数据操作方式。
# 双端队列允许两端添加或删除元素，可以使用collections模块中的deque实现

