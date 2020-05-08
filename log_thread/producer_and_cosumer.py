# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 04/05/2020 14.48

import  threading
import  time


condition  = threading.Condition()
products = 1


class Consumer(threading.Thread):

    def run(self) -> None:
        global condition, products
        while True:
            if condition.acquire():
                if products >= 1:
                    products -= 1
                    print("{}:{}->我消费了一件商品，现在商品的数量是{}".format("消费者",threading.currentThread().getName(), products))
                    condition.notify()
                else:
                    print("{}:{}->没有库存了，现在商品的数量是{}".format("消费者",threading.currentThread().getName(), products))
                    condition.wait()
                condition.release()
                time.sleep(2)


class Producer(threading.Thread):

    def run(self) -> None:
        global condition, products
        while True:
            if condition.acquire():
                if products <= 2:
                    products += 1
                    print("{}:{}库存不足，数量为{}，努力生产".format("生产者", threading.currentThread().getName(),products))
                    condition.notify()   # 唤起一个等待的线程    notifyall 唤醒所有线程
                else:
                    print("{}:{}库存充足，数量为{}，休息一会儿".format("生产者", threading.currentThread().getName(), products))
                    condition.wait()    # 线程等待    ? debug 会停在这里
                condition.release()
                time.sleep(2)




if __name__ == "__main__":
    for i in range(2):
        c = Consumer()
        c.start()

    for i in range(3):
        p = Producer()
        p.start()






























