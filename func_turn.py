
# def func4():
#     return 1,2
# x,y = func4()
# print(x)
# print(y)

# 函数的返回值是一个函数
def func5(x):
    if x == 2:
        def inner_func(y):
            print("inner1")
            return  y*y
    if x == 3:
        def inner_func(y):
            print("inner2")
            return y*y*y
    return  inner_func
calc = func5(3)
z = calc(4)
print(z)