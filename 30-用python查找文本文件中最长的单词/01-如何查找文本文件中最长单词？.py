







def find_longst_word(file_path):
    longst_word = ''
    try:
        with open(file_path,'r')as file:
            for line in file:
                words = line.split()
                for word in words:
                    if len(word)>len(longst_word):
                        longst_word = word
        return longst_word
    except FileNotFoundError:
        print('文件不存在')


file_paths = '1.txt'
txt = find_longst_word(file_paths)
print(txt)
