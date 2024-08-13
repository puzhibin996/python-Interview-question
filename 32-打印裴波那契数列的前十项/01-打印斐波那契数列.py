#
#
# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2,n):
#         next_value = fib_sequence[-1]+fib_sequence[-2]
#         fib_sequence.append(next_value)
#     return fib_sequence
#
# print(fibonacci(10))
#
#
# #斐波那契数列的定义：数列的前两项是0和1，之后每一项是由前两项之和构成的，所以，我们可以先定义数列的前两项，然后使用循环来生成并打印后面的项。
#
#
# # 递归版本：除了用循环来生成斐波那契数列，还可以使用递归的方法，递归的方法较为直观，但在效率上可能不如迭代的方法，因为递归方法容易造成重复计算。
# def fibonacci_recursive(n):
#     if n <=0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n ==2:
#         return [0,1]
#     else:
#         seq = fibonacci_recursive(n-1)
#         seq.append(seq[-1]+seq[-2])
#         return seq
# print(fibonacci_recursive(10))


# 测试