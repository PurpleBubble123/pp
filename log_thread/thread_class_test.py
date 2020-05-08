# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 04/05/2020 05.40

from threading import Thread


class Hello(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name


    def run(self):
        print("hello %s " % self.name)


t = Hello("我是一个线程的类")
t.start()   # 自动调用run方法
print("我是主线程")

