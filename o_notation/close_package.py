# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 28/04/2020 14.34

"""
闭包：外部函数的返回值是内部函数的引用
"""

def outer(a):
    b = 10
    def inner():
        print(a + b)
    # 外部函数的返回值是内部函数的引用
    return inner

inner_func = outer(5)
inner_func()

