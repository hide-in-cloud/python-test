import queue
import random
import threading
import time


def produce(q):
    for i in range(10):
        time.sleep(1)
        num = random.randint(1, 100)
        q.put(num)
        print("生产者产生数据：%d" % num)
    q.put(None)
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者获取到：%d" % item)
        time.sleep(3)
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)
    arr = []
    t1 = threading.Thread(target=produce, name='生产者', args=(q,))
    t1.start()
    t2 = threading.Thread(target=consume, name='消费者', args=(q,))
    t2.start()

    t1.join()
    t2.join()
