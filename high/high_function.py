# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 01/05/2020 09.05

# Lambda表达式   又叫匿名函数
# 格式: lambda 参数列表：表达式


f = lambda  x: x + x

r = f(1)
# print(r)

# map 函数: 迭代传参入函数进行计算,返回的是地址
map_demo = map(f, [1, 2, 3, 4])
# print(map_demo)
# print(list(map_demo))
#
# print(list(map(str,[1, 2, 3, 4])))


# reduce 函数: 将前一个元素计算运行的结果作为第一参数传进去
from functools import reduce
r = reduce(lambda  x,y:x+y, [1, 2, 3, 4],10)
#print(r)


# filter 函数

print(list(filter(lambda x: x % 2 ==1 ,[1, 2, 3, 4, 5, 6, 7, 8  ])))

print(list(filter(lambda x: x and x.strip(), ["1", "aa", " ", None])))


