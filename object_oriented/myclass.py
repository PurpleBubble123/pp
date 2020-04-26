# It is a nice day. Let's get start
__author__ = "boya"
__date__ =  ""

"""
名词：类、对象、实例、实例化
类：代表具有相同特征的一类事物（人）
对象和实例：具体的某一事物或人
实例化：将类变成对象的过程，new一个对象
"""

"""
python 命名规范
类：驼峰命名法 PersonStudyEnglish
其他：包名、模块名、方法名、函数名、变量名 皆采用小蛇命名法 person_study_english
"""



# 函数 方法

def func1():    # 在模块中声明的叫函数
    pass

class Person:

    def func2(self):    # 在类中声明的叫方法
        pass
    # 类变量，属性,必须有默认值，可为空
    name = "aa"
    age  = 10000
    # 类私有变量
    __private_args = "class private"

    # # 无参数的构造函数
    # def __init__(self):
    #     print("构造函数运行")

    # 有参数的构造函数
    def __init__(self,name,age,sex):
        # print(name)
        # print(age)

        # 实例变量
        self.name = name
        self.age = age
        self.sex = sex
        print(self.name)
        print(self.age)
        print(self.sex)

    # 给外部提供私有变量
    def get_private_args(self):
        return self.__private_args
    # 私有方法
    def __my_private_method(self):
        print("私有方法")

    # 保护方法
    def  _my_protected_method(self):
        print("保护方法")

    # 类方法,需有装饰器
    @classmethod
    def my_class_method(cls):
        print("类方法")

    # 静态方法
    @staticmethod
    def my_static_method():
        print("静态方法")


# p = Person()
# print(p.name)

p = Person("bb",12000,"M")
print(p.get_private_args())

r = Person.get_private_args(p)
print(r)

# 静态方法调用，工具类可能会调用
Person.my_static_method()

# 类方法调用
Person.my_class_method()

# Python中，私有方法能否访问
# 能，通过类调用
print(Person.__dict__)   # 所有的变量和方法
print(p._Person__private_args)
p._Person__my_private_method()





