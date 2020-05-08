# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 04/05/2020 11.42

############ 多线程事件 ###############
# 事件 (event)
"""
线程间的通信
"""
import  threading, time

class Boss(threading.Thread):
    def run(self) -> None:
        print("Boss: 996 begin")
        # 事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("Boss: finish no 996")
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def run(self) -> None:
        event.wait()
        print("Worker: what? why 996")
        event.clear()
        event.wait()
        print("worker: good")

if __name__ == "__main__":
    event = threading.Event()

    # 线程数
    threads = []
    for i in range(5):
        threads.append(Worker())

    threads.append(Boss())

    for t in threads:
        t.start()











