# python中常见的数据结构有：
# 1. ————————————————————————————————字符串————————————————————————————————
# 、


# 创建字符串 单引号
str1 = '我是一个单引号字符串'
print(str1)

# 创建字符串 双引号
str2 = "我是一个双引号字符串"
print(str2)

# 创建爱你一个三引号 ''' 或者 """ 用于多行字符串
str3 = '''我是第一行字符串
            我是第二行字符串'''
print(str3)

# 访问字符串中的字符
# 索引访问
first_char = str3[0]
print("访问字符串的0：", first_char)

# 切片访问
substring = str3[3:8]
print("访问字符串的3-8：", substring)

# 字符串拼接
# 使用加号
str4 = str3 + str1
print("使用加号拼接：",str4)

str5 = "Hello " + ','+ 'puzhibin'
print("使用创建拼接：",str5)

# 使用格式化字符串f-string
name = "puzhibin"
message = f"Hello {name}"
print("使用格式化字符串f-string：",message)

# 使用format（）方法
age = "12"
message_age = "你现在年龄是{}！".format(age)
print("使用format（）方法：",message_age)


# 字符串方法
# len（s） 获取字符串长度
length = len(str3)
print("字符串长度：",length)

# str.lower() 将所有字符串转换为小写
str6 = "ABCD,S1234adfbsAFJOO"
lower_str = str6.lower()
print("将所有字符串转换为小写：",lower_str)

# str.upper() 将所有字符串转换为大写
upper_str = str6.upper()
print("将所有字符串转换为大写：",upper_str)

# str.strip()  str.lstrip()  str.rstrip() 去除字符串前后的空白字符
str7 = "   hello world   "
strip_str = str7.strip()
lstrip_str = str7.lstrip()
rstrip_str = str7.rstrip()
print(f"strip 去除空白：{strip_str}//lstrip 去除空白：{lstrip_str}//rstrip 去除空白：{rstrip_str}")


# str.split(sep=None) 根据分隔符字符串分割成列表
split_str = str7.split(' ')
print("str.split(sep=None) 根据分隔符字符串分割成列表：",split_str)
str8 = 'hello,puzhibin,996'
split_str1 = str8.split(',')
print("str.split(sep=None) 根据分隔符字符串分割成列表：",split_str1)


# str.join(iterable) 将列表中字符串连接起来，使用指定的字符串作为分隔符。
join_str = "-".join(split_str1)
print("join将列表字符串连接起来：",join_str)

# str.replace(old,new ) 替换字符串中的某个子串
replace_str = str8.replace('puzhibin','puzhibin是个大帅哥！')
print("replace替换字符串中的某个子串：",replace_str)


# str.startswith(prefix),str.endswith(suffix) 检查字符串是否以特定的前缀或后缀开始/结束
startswith_str = str8.startswith('hello')
print("startswith检查字符串是否以特定的前缀开始：",startswith_str)
endswith_str = str8.endswith('996')
print("endswith检查字符串是否是以特定的后缀开始：",endswith_str)


# str.find(sub)  str.index(sub) 查找字符串的位置， find（） 在找不到子字符串时返回 -1 ，
# 而 index（） 会爆出异常
find_str = str8.find('puzhibin')
print("find查找字符串的位置：",find_str)
index_str = str8.index('996')
print("index查找字符串的位置：",index_str)


# str.isalpha()  str.isdigit()  str.isalnum()  str.islower()  str.isupper() 检查字符串是否全部有字母、数字、字母数字、空格、小写或大写字符组成


# 字符串格式化
#  使用% 符号进行格式化
formatted = "Hello,%s!"% name # %s 表示字符串，%d 表示数字，%f 表示浮点数，%i 表示整数，%c 表示字符，%b 表示二进制，%o 表示八进制，%x 表示十六进制
print("使用% 符号进行格式化：",formatted)


# 重复字符串
repeated ="-" * 10
print("重复字符串：",repeated)

# 字符串比较
s1 = "hello world"
s2 = "hello world"
if s1 == s2:
    print("字符串比较：",s1 == s2)

# 检查成员
if 'puzhibin' in str8:
    print("检查成员：",'puzhibin' in str8)



# 总结：
# 字符串是一个不可变的序列类型，但在很多情况下可以将其视为一种数据结构
# 使用单引号，双引号，来定义
# 支持索引访问，切片访问，字符串拼接。





