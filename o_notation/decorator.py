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
# eg.3 多个参数
def many_args(function_name):
    def warpper(*args):
        print(*args)
        function_name(*args)
    return warpper


@many_args
def function_demo3(*args):
    print(*args)


#function_demo3(1,2,3,4,5,6)


########################
# eg.4 key:value类型参数

def dict_args(function_name):
    def wrapper(**kwargs):
        print(kwargs)
        function_name(**kwargs)
    return wrapper


@dict_args
def function_demo4(**kwargs):
    print(kwargs)


#function_demo4(name = "aaa", age = 10)


#########################
# eg.5 组合类型参数

def combo_args(function_name):
    def w(*args, **kwargs):
        print(args,kwargs)
    return w


@combo_args
def function_demo5(*args, **kwargs):
    pass


#function_demo5(1,2, name = "aaa", age = 10)


##########################
# eg.6 终极：最大运行时间


def max_runtime(timeout):
    def out_wrapper(function_name):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            i = function_name()
            end_time = time.time()
            use_time = end_time - start_time

            if use_time >timeout:
                print("函数运行超时")
                #raise RuntimeError ("函数运行超时")
            return i # 函数返回值
        return wrapper
    return out_wrapper




@max_runtime(timeout = 3)
def function_demo6(*args, **kwargs):
    time.sleep(2)
    print("demo6运行")
    return  1


r = function_demo6()
print(r)