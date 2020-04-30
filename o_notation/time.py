# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 28/04/2020 08.59

a = 0
n = 100

while a < n:
    a = a + 1

#此例时间复杂度是O（N） N为常数 计算量为n 括号里放的就是计算量

a = 0
b = 0
c = 1
n = 100
while a < n:
    while b < n:
        c = (c + 1) **2  # 计算表达式 时间复杂度是 O(N^2)
        b = b + 1
    a = a + 1

a = 0
b = 0
n = 100
while a < n:
    while b < n:
        c = (c + 1) ** 2
        b = b * 2
    a = a + 1

# 此例时间复杂度的标识 O(NlogN)












