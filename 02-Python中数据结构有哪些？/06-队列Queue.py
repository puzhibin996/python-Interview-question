# python中常见的数据结构有：
# 1. ————————————————————————————————队列————————————————————————————————
import queue
from collections import deque

# 使用list作为队列 ，list在亮度的操作效率不同，但可以用来简单的模拟队列行为
# 创建队列  入队
queue1 = []
queue1.append('first item')
queue1.append('second item')
print(queue1.pop(0)) # 出队 ，输出first item


# 使用collections.deque 作为队列
# collections.deque是双向队列，适用于快速的两端操作，因此用作队列时比list更有效率
queue2 = deque()
queue2.append('我是第一个')
queue2.append('我是第二个')
print(queue2.popleft())

#使用queue.Queue作为队列
# queue.Queue是线程安全的队列，适合在多线程中使用
q = queue.Queue()
q.put('string1 string')
q.put('string2 string')
print(q.get())
print(q.get())

# 总结：
# 入队： 向队列尾部添加一个元素
# 出队： 从队列头部移除并返回一个元素，这是FIFO原则的体现。
# 检查队列是否为空： 在执行出队操作前，通常需要检查队列是否为空，以避免产生错误。
# 获取队列大小： 有时需要知道队列中有多少元素，这在资源管理或调度中很有用
# 线程安全： 在多线程环境下，队列需要保证现场安全，防止数据竞争条件。

# 队列的其它特性
# 阻塞队列： queue.Queue 允许你创建阻塞队列，当队列满脸，put（）操作会阻塞，知道队列有空间
#           当队列空时，get（）操作会阻塞，直到队列中有元素
# 优先级队列： queue.PriorityQueue 是一个特殊类型的队列，其中元素按照优先级排序。
#           这在任务调度中特别有用，高优先级的任务会被优先处理。

# 队列的应用
# 任务调度： 在一个程序中，队列可以用来按顺序安排任务的执行
# 消息传递： 在多进程或多线程环境中，队列可以作为消息传递的通道
# 缓存： 队列可以用于缓存数据，当缓存满时，新数据会替换最旧的数据
# 缓冲区： 在网络编程中，队列看用来缓冲输入和输出数据
# 队列是一种先进先出的数据结构FIFO，可以使用collections模块中的deque实现

