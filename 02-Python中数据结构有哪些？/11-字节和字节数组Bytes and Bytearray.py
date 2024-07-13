# python中常见的数据结构有：
# 1. ————————————————————————————————字节和字节数组————————————————————————————————

# bytes 类型
# bytes是一个不可变的序列类型，它包含整数0-255的序列。一旦创建，其内容不能改变。你可以通过bytes对象创建

# 从列表或元祖创建：
b = bytes([1,2,3,4,5])
print(b)

# 从字符串编码创建
b1 = b'puzhibin'
print(b1)
b2 = 'puzhibin'.encode('utf-8')
print(b2)

# 从一个范围创建
b3 = bytes(range(0,256))
print(b3)

# bytearray 类型
# bytearray类似于bytes，但它是可变的，这意味着你可以修改其内容。这在需要频繁修改字节序列时很有用。
# 创建bytearray的方法与bytes类似，但是使用bytearray（） 函数

# 从列表或元祖创建
ba = bytearray([1,2,3,3,4,5,65,23])
print(ba)

# 从字符串编码创建
ba1 = bytearray(b'puzhibin996')
print(ba1)
ba2 = 'hello puzhibin'.encode('utf-8')
print(ba2)

# 初始化为特定长度
ba3 = bytearray(222)
print(ba3)

# 修改bytes是不可变的
ba4 = bytes([1,2,3])
try:
    ba4[0] = 5
except TypeError as e:
    print("error",e)

# 修改bytearray是可变的
ba5 = bytearray([1,2,4])
ba5[0] = 5
print(ba5)

# 字节拼接
ba6 = bytes([4,5,6])
ba7 = bytes([1,2,3])
b_concat = ba6+ba7
print("Concatenated bytes:",b_concat)


# 字节解码回字符串
ba8 = b'puzhibin996'.decode('utf-8')
print("字节解码为字符串:",ba8)

# 字符串编码成字节
ba9 = 'world puzhibin'.encode('utf-8')
print("字符串编码为字节:",ba9)


# 文件读写
with open('puzhibin.txt','wb')as f:# 以二进制写入
    f.write(b'123456')

with open('puzhibin.txt','rb')as f:# 以二进制读取
    content = f.read()
    print("File content:",content)



# bytes 和 bytearray 类型用于处理二进制数据。他们在处理网络通信、文件读写、加密解密等场景中非常有用。
# bytes
# 字节是不可变的字节序列，用于处理二进制数据。使用 ’b‘ 定义。
# 字节数据是可变的字节序列，使用bytearray函数创建。




