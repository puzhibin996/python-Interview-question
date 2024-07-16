import re

# 正则表达式是一种强大的文本匹配工具，可以用于查找、替换或提取附和特定模式的文本。
# 在python中 re模块提供了对正则表达式的支持


# 基本概念。
# . ：匹配任何单个字符（除了换行符）
# ^ ：表示行的开始
# $ ：表示行的结束
# * ：表示前面的字符可以出现零次或多次
# + ：表示前面的字符串至少出现一次
# ？：表示前面的字符可以出现零次或一次。
# [] ：定义一个字符集，匹配其中的任何一个字符。
# （） ：定义一个子表达式，可以用于分组。
# | ：选择运算符，表示或关系
# \d :匹配任何数字
# \w ：匹配任何字母数字字符和下划线
# \s :匹配任何空白字符
# \b :单词边界

# 查找所有匹配项
text = "ABsdadfwbOAJOFAJ adsfa AJgasdA  AOIAEMSosdfjoA  AOFJOSFJHOlsjdfklsjdf "
pattern = r'A'
matches = re.findall(pattern,text)
print(matches)


# 替换匹配项
new_text = re.sub(pattern,"puzhibin",text)
print(new_text)


# 查找第一个匹配项
text1 = "puzhibin,123ppsds,la"
pattern1 = r'pu'
match = re.search(pattern1,text1)
if match:
    print(match.group())# 输出pu


# 搜索模式并获取分组
text2 = "My phone number is 123-456-7890."
pattern2 = r"(\d{3})-(\d{3})-(\d{4})"
match1 = re.search(pattern2,text2)
if match1:
    print("Area Code:",match1.group(1))
    print("Exchange:",match1.group(2))
    print("Line Number:",match1.group(3))


# 编译正则表达式
regex = re.compile(pattern2)
match3 = regex.search(text2)
print(match3.group())


# 复杂示例 ： 提取电子邮件地址
text4 = """
John Doe <john.doe@example.com>
Jane Smith <jane.smith@example.com>
"""
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(email_pattern,text4)
print(emails)

# 以上示例展示了如何在python中使用正则表达式进行文本匹配、搜索、替换和提取。
# 正则表达式可以非常强大，但也可能变得复杂，因此在编写复杂的正则表达式，确保进行充分的测试和验证。





