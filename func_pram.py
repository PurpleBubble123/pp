
# 关键字参数
# def my_func_1(name,age):
#     print(name)
#     print(age)
#
# my_func_1(name=1,age=2)


# 默认参数
# def my_func_2(name = "zhou", age  = 30):
#     print(name)
#     print(age)
#
# my_func_2()
# my_func_2("li",40)

# def my_func_3(name,age = 50):
#     print(name)
#     print(age)
#
# my_func_3(2)
# my_func_3(2,3)


# 递归：自己调用自己（在函数内部进行调用）,***必须明确结束条件***
# def my_func_4(x):
#     print(x)
#     my_func_4(x+1)

# 函数的返回值
# def f(x):
#     # 明确返回条件
#     return "传入" + str(x)
#
# r = f(1)
# print(r)

def f(x):
    # 明确递归结束条件
    if x ==1:
        return 1

    return x + f(x-1)





