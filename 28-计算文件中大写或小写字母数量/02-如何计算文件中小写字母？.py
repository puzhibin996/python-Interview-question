

# 打开文件
# 读取文件
# 遍历文件
# 计数量

def min_txt(file_path):
    with open(file_path, 'r') as f:
        # 读取文件
        lines = f.read()
        # 遍历出小写字母数量
        count = 0
        for line in lines:
            if line.islower():
                count += 1
        return count

file_path = '1.txt'
min_nums = min_txt(file_path)
print("小写字母数量为：",min_nums)
