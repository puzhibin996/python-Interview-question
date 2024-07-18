



# filter() 函数也可以用于过滤字符串中的字符

text = "puzhibin is boy,Hello World"
# 过滤处素有大写字母
uppercase_letters = filter(lambda c: c.isupper(),text)

uppercase_letters_list = list(uppercase_letters)
print(uppercase_letters_list)


# filter() 返回的是一个迭代器，所以如果你需要多次使用结果，应该先将其转换为列表或其他可重复使用的容器类型。
# 如果你传递给filter（）的函数总是返回True，那么filter（）函数会返回一个包含所有元素 迭代器。
# 如果没有提供函数，filter（）会默认使用一个布尔化函数，过滤掉素有被视为false元素，（如空字符串、0、None等）
