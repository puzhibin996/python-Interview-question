



# python中for和while循环可以与else子句一起使用，这种结构可能看起来有些不寻常，因为通常else子句与if语句相关联。
# 然而 再循环中加入else子句有其特定的用途和逻辑


# for-else 结构在循环正常完成，既没有被break语句中断，后执行else块中的代码。
# 如果循环被break语句提前终止，则else块不会执行。

numbers = [1,2,3,4,5,6]
for number in numbers:
    if number == 4:
        print("判断到4了，结束循环")
        break
else:
    print("循环正常完成，没有被break语句中断")


# 上面的代码示例中，else块将不会执行，因为列表中有4这个元素。所以break语句被执行，导致循环提前终止。
















