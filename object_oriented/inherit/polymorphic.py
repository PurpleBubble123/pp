# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 27/04/2020 15.00

"""
多态：一类事物有多种形态
多态性：
"""
from abc import ABCMeta, abstractmethod


class Animal:
    def run(self):
        raise AttributeError("子类必须实现这个方法")

class Person(Animal):
    #pass
    def run(self):
        print("人走")

class Pig(Animal):
    def run(self):
        print("pig run")

class Dog(Animal):
    def run(self):
        print("dog run")

person = Person()
person.run()

pig = Pig()
pig.run()

dog = Dog()
dog.run()

"""
多态性
"""

def func(obj):
    obj.run()

# 往USB里插入设备
# func(person)
# func(pig)
# func(dog)

class Computer(metaclass=ABCMeta):

    @abstractmethod # 不能实例化一个包含抽象方法的类
    def usb_insert(self):
        pass

class ThinkPad(Computer):
    def usb_insert(self):
        pass

    def usb_run(self,sub_computer):
        sub_computer.usb_insert()


class Mouse(Computer):
    def usb_insert(self):
        print("insert mouse")

class Kerboard(Computer):
    def usb_insert(self):
        print("insert keyboard")

# buy a computer
computer = ThinkPad()

# buy a mouse
m = Mouse()
# insert mouse
#usb_run(m)
computer.usb_run(m)

# buy a keyboard
k = Kerboard()
#usb_run(k)
computer.usb_run(k)


