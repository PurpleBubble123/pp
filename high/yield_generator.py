# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 01/05/2020 14.09

# 生成器


def demo1():
    l = [x for x in range(1000)]
    return  l

# a = demo1()
# print(a)


def yield_demo2():
    for x in range(3):
        yield x
        print("生成器后")
    print("生成器外层")

b = yield_demo2()
#print(b)

# for i in b:
#     print(i)
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())


# 多生成器

def yield_demo3():
    a = 10
    b = 20
    c = 30
    for x in range(3):
        yield a
        print("生成a之后")
        yield b
        print("生成b之后")
        yield c
        print("生成c之后")

g = yield_demo3()
for gg in g:
    print(gg)



