# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 27/04/2020 13.06

class A(object):
    def test(self):
        print("A class")

class B(A):
    def test(self):
        print("B class")

class C(A):
    def test(self):
        print("C class")

class D(B):
    def test1(self):
        print("D class")

class E(C):
    def test(self):
        print("E class")

class F(D,E):
    pass

f = F()
f.test()

print(F.__mro__)   # 呈现继承顺序

"""
(<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
F-->D-->B-->E-->C-->A
"""
