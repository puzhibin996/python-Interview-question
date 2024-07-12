# python中常见的数据结构有：
# 1. ————————————————————————————————堆————————————————————————————————
import heapq

# 创建一个空列表，用于存放堆
heap = []

# 使用heappush将元素推入堆中
heapq.heappush(heap,5)
heapq.heappush(heap,4)
heapq.heappush(heap,99)
print(heap)

# 使用heappop从堆中弹出最小的元素
print(heapq.heappop(heap))

# heapify将一个列表转换为堆
data = [5,3,32,223,434,21]
heapq.heapify(data)
print("heapify 列表转换为堆：",data)


# 使用heapreplace同时弹出最小元素并推入新元素
heapq.heapreplace(data,23)
print("heapreplace 最小元素和推入新元素：",data)


# 使用merge 合并两个已排序的列表
merged = heapq.merge(data,[22,33,44,55,66])
print("merge 合并两个已排序的列表：",list(merged))


# 使用nlargest 和nsmallest 找到最大的n个和最小的n个元素
print("nlargest最大n个元素：",heapq.nlargest(2,data))
print("nsmallest最小n个元素：",heapq.nsmallest(2,data))



# 总结
# 堆 是一种特殊的树形数据结构，通常用于实现优先队列，堆的特点是他满足堆属性：
#       父节点的值总是小于最小堆或大于最大堆的子节点值。
# 堆通常使用数组来实现，通过索引操作来模拟树的结构
# python标准款中heapq模块提供了最小堆操作。heapq模块中的函数通常假设堆事在列表的第一个元素开始的，
#   即索引0处，而不是像在一些其它语言中那样从1开始
# 常见heapq模块函数
# heappush(heap,item):将item推入堆中，维持堆的性质
# heappop（heap）：从堆中弹出最小的元素，并维持堆的性质。
# heapify（x）：将列表x就地转换为堆
# heapreplace（heap，item）：弹出并返回堆中的最小元素，同时将item推入堆中。
# merge（*iterables，key=None，reverse=False）：合并多个已排序的输入迭代器，返回一个已排序的迭代器
# nlargest(n,iterable,key=None):返回iterable中最大的n个元素
# nsmallest（n,iterable,key=None）:返回iterable中最小的n个元素

# 堆的应用
# 优先队列： 堆可以用于实现优先队列，其中每个元素都有一个优先级，优先级最高的元素将被优先处理。
# 排序算法： 堆排序利用堆的性质来对元素进行排序
# 查找最小火最大值： 堆可以快速第找到一组数据中的最小或最大值，而无需对整个数据进行排序
# 算法实现： 堆在Dijkstra算法、Prim算法等图算法中用于存储处理节点，以便更快速的找到下一个最低成本的节点。
# 堆是一种特殊的树形结构，常用语实现优先队列。

