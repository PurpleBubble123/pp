# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 30/04/2020 17.27

"""
函数的参数
- 必须参数(必须放在最前面）
- 默认参数、组合参数
- 函数作为参数
- 对象作为参数
- **kwargs: 关键字参数
- *args: 可变参数

"""


def function(a, b, *args, **kwargs):
    print(a,b)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))


# function(1,2,3,4,5,6, name = 666)


# 命名关键字参数，*后边的必须写名字
# 命名关键字参数是必须参数，如果不需要他是必须参数，那么给以给一个默认值
def func2(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# func2(1, 2, c = 3, d = 4)
# func2(1, 2, c = 4, d = 3)


def func3(a, b, c):
    print(a)
    print(b)
    print(c)


# s = (1, 2, 3)
# func3(*s)   # 将可迭代的对象拆开，给到对应的位置上
# s1 = [4, 5, 6]
# func3(*s1)


kw = {"a":1, "b":2, "c":3}
func3(*kw)   # 传键的名字，键的名字需与赋值名保持一致
func3(**kw)  # 一般传字典类型的时候，用这种方式 **




