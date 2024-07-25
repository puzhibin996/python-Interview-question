





# 实例属性和类属性
# 实例属性是每个实例中独立存在的属性，而类属性是所有实例共享的属性。下面是定义实例属性和类属性的例子
### 实例属性
# 实例属性是通过实例方法（如果构造函数__init__）定义的，每个实例都有自己的副本。
class MyClass:
    def __init__(self,instance_attribute):
        self.instance_attribute = instance_attribute

# 创建实例并设置实例属性
instance1 = MyClass("instance 1")
instance2 = MyClass("instance 2")

print(instance1.instance_attribute)
print(instance2.instance_attribute)

### 类属性
# 类属性是通过在类体内部直接定义变量来创建的，所有实例共享同一个值
class MyClass1:
    class_attribute = "this is a class attribute"

# 访问类属性
print(MyClass1.class_attribute)

instance3 = MyClass1()
instance4 = MyClass1()

print(instance3.class_attribute)
print(instance4.class_attribute)

# 修改类属性
MyClass1.class_attribute = "new value for class attribute"
print(instance3.class_attribute)
print(instance4.class_attribute)


# 在上面示例代码中，MyClass1包含了一个类属性class_attribute，当修改类属性时，所有实例都会受到影响。