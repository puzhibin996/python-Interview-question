# python中常见的数据结构有：
# 1. ————————————————————————————————栈————————————————————————————————
from collections import deque

# 使用列表模拟栈
# 列表的 append（） 方法可以用来想栈顶 添加元素，而pop（）方法可以从栈顶移除元素，这恰好符合栈的工作原理

# 创建栈
stack = []
#入栈操作
stack.append('A')
stack.append('B')
stack.append('C')
#出栈操作
a = stack.pop()
b = stack.pop()
print(a)
print(b)


# 使用collections.deque作为栈
# collections.deque是一个双向队列，可以高效地在两端进行操作，因此也可以作用栈
stack_deque = deque()
stack_deque.append('1')
stack_deque.append('2')
stack_deque.append('3')
print(stack_deque.pop())




# 总结：
# 栈 尊许后进先出原则的数据结构，也就说最后放入栈中的元素，将最先被去除。
# python没有内置的栈数据类型，我们可以通过列表List，来模拟栈的行为。
# 并且python提供collections模块，还可以了一个deque类。

# 栈的主要操作和意义
# 入栈：向栈顶添加一个元素
# 出栈：移除并返回栈顶的元素
# 查看栈顶元素：查看栈顶元素而不溢出它，可以使用[-1]索引
# 检查栈是否为空：可以使用not stack 或 len（stack） == 0 来检查栈是否为空。

# 栈的应用
# 函数调用和局部变量管理：在编程语言中，每当函数被调用时，局部变量和返回地址都会被压入栈中，函数返回时这些信息会被弹出栈。
# 表达式求值与转换： 栈可以用于计算逆波兰表示法RPN，或中缀表达式的值，也可以用于将中缀表达式转换为后缀表达式。
# 括号匹配： 栈可以用来检测括号是正确匹配对

# 栈是一种后进献出LIFO 的数据结构，通常可以使用列表实现。
















