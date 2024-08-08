import re


def find_longst_word(file_path):
    longst_word = ''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b',content)
            for word in words:
                if len(word)>len(longst_word):
                    longst_word = word
        return longst_word
    except FileNotFoundError:
        print('文件不存在')

txt = '1.txt'
longst = find_longst_word(txt)
print(longst)

# 在这里，引入了re模块，并使用正则表达式\b\w+\b 提取出所有单词，从而更精准的处理文本内容。这种方法比普通的按空格更为灵活和强大。
