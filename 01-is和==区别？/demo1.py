class TestCase:
    def __init__(self,name,result):
        self.name = name
        self.result = result



test1 = TestCase('zhangsan','Pass')
test2 = TestCase('zhangsan','Pass')

# 我们使用 == 来比较他们
print(test1 == test2)
# 打印结果为 True ，因为== 比较的是对象的内容，所以结果是True


test1 = TestCase('zhangsan','Pass')
test2 = TestCase('zhangsan','Pass')
# 如果我们用is 来比较他们
print(test1 is test2)
# 打印结果为 False ，因为is 比较的是对象的身份（内存地址），所以结果是False

# 中文总结
# 在项目中，当你需要比较两个对象是否在内存中是同一个实例时，应该使用 is 运算符。
# 例如，比较两个变量是否引用了同一个测试用例实例。相反，当你需要比较两个对象的内容是否相同时，
# 应该使用 == 运算符。例如，比较两个测试用例的结果是否相同