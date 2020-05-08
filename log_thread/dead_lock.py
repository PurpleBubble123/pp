# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 04/05/2020 12.35

# 多线程锁 死锁
import time
from threading import Thread, currentThread, RLock,Lock

# 互斥锁
# mutexA = Lock()
# mutexB = Lock()

# 递归锁
mutexA = RLock()
mutexB = RLock()
class House(Thread):
    def run(self) -> None:
        self.room1()
        self.room2()

    def room1(self):
        mutexA.acquire()
        print(currentThread().name + "房间1拿到A锁")
        mutexB.acquire()
        print(currentThread().name + "房间1拿到B锁")
        mutexB.release()
        print(currentThread().name + "房间1释放B锁")
        mutexA.release()
        print(currentThread().name + "房间1释放A锁")


    def room2(self):
        mutexB.acquire()
        print(currentThread().name + "房间2拿到B锁")
        time.sleep(1)
        mutexA.acquire()
        print(currentThread().name + "房间2拿到A锁")
        mutexA.release()
        print(currentThread().name + "房间2释放A锁")
        mutexB.release()
        print(currentThread().name + "房间2释放B锁")


if __name__ == "__main__":
    for i in range(10):
        t = House()
        t.start()







