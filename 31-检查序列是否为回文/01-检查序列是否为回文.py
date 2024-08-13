




def is_palindrome(sequence):
    return sequence ==sequence[::-1]

print(is_palindrome("puzhibibn"))
print(is_palindrome("radar"))


# 回文序列（Palindrome）是指正正序和倒序读起来都一样的序列。检查一个序列是否有回文序列只需要将其颠倒过来与原序列比较即可。
# 我们可以利用切片（slicing）快速反转序列，然后进行比较。

# 扩展知识
# 1.切片（slicing） 在python中，序列（如字符串、列表、元祖等）支持切片操作。sequence[::-1]就是通过[::-1]切片创建了一个反向的副本。
# 2.双指针：虽然切片操作简单，但对于大型序列，生成一个新的序列会占用额外的空间。
#       我们可以使用双指针方法来避免这一问题，即从序列两端同事向中间移动比较元素。

def is_palindromes(sequence):
    left,right = 0,len(sequence) -1
    while left < right:
        if sequence[left] != sequence[right]:
            return False
        left += 1
        right -=1
    return True

# test
print(is_palindromes("radar"))
print(is_palindromes([1,2,3,2,1]))
print(is_palindrome("hello"))

# 适用场景：这个检查回文的函数不仅可用于字符串，还能应用于其他序列类型，比如列表，元祖等。
# 边界情况：需要逐一处理一些特殊情况，比如空序列或者单个元素的序列，他们应该也被认为是回文序列。