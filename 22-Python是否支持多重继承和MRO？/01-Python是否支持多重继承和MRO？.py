







# python支持多重继承，这意味着一个类可以从多个父类继承属性和方法。多重继承可以让你组合不同类的功能，使得类的设计更加灵活和强大
class Animal:
    def speak(self):
        print("An animal speaks!")
class Mammal:
    def walk(self):
        print("A mammal walks!")
class Dog(Animal,Mammal):
    def bark(self):
        print("Woof woof!")

dog = Dog()
dog.speak()
dog.walk()
dog.bark()
# 在上面代码中，Dog类继承了Animal和Mammal两个类，Dog类可以访问这两个父类的方法，如speak（）和walk（）


### MRO （Method Resolution Order）
# MRO（方法解析顺序）是python中用于确定多重继承类种方法调用的顺序的规则。
# python使用C3线性化算法来决定多重继承中方法的调用顺序，确保方法调用的顺序是一致和可预测的。
# MRO的规则
# 1.左至右：在多个父类的情况下，从左至右一次查找。
# 2.深度优化：优先考虑当前类的父类，然后是父类的父类，以此类推。
# 3.C3线性化：这是一种广义的左至右算法，确保所有父类的方法仅被考虑一次，并且按照一定的顺序排列。
class A:
    def do_it(self):
        print("this is A")
class B(A):
    def do_it(self):
        print("this is B")
        super().do_it()
class C(A):
    def do_it(self):
        print("this is C")
        super().do_it()
class D(B,C):
    def do_it(self):
        print("this is D")
        super().do_it()

d=D()
d.do_it()
print(D.mro())