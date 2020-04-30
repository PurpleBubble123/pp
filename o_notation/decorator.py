# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 28/04/2020 15.21

"""
装饰器 （语法糖、注解）
"""


# def func_1(x):
#     return x * 2
#
#
# def func_2(x):
#     return x * 3
#
#
# def func_3(x, y, i, j):
#     return x(i) + y(j)
#
#
# r = func_3( func_1, func_2, 2, 3)
# print(r)
import time


##############
# eg.1 没有参数
def runtime_noargs(function_name):
    def wrapper():
        start_time = time.time()
        print("函数运行前")
        function_name()
        print("函数运行后")
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


@runtime_noargs
def function_demo1():
    time.sleep(1)
    print("demo1函数运行")


# function_demo1()


##############
# eg.2 一个参数
def args_is_str(function_name):
    def wrapper(args):
        t = type(args)
        if not isinstance(t(),str):   # 判断参数是否为str
            print("参数错误")
        else:
            function_name(args)
    return wrapper

@args_is_str
def function_demo2(args):
    print(args)

#function_demo2(1)
#function_demo2("aaaa")


######################
# eg.3