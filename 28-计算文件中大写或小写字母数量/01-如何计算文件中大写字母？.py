


# 从题目可知道如下步骤。
# 打开文件并读取内容
# 初始化一个计数器来记录大写字母的数量。
# 遍历文件内容的每个字符
# 使用isupper（）方法检查字符是否为大写字母
# 如果字符为大写字母，则计数器加一
# 输出计算器的值。



# 实际代码如下：
def count_txt(file_path):
    try:
        # 打开文件
        with open(file_path,'r')as file:
            # 读文件
            content = file.read()
        # 遍历出现大写字母
        new_count = sum(1 for char in content if char.isupper())
        # 返回大写字母的数量
        return new_count
    except FileNotFoundError:
        print("文件不存在")
        return 0

file_path = '1.txt'
count_nums = count_txt(file_path)
print("大写字母的数量为：",count_nums)
