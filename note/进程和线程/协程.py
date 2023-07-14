import time
import greenlet
import gevent
from gevent import monkey

'''
grennlet:手动切换线程
gevent:自动切换
'''

monkey.patch_all()  # 辅助补丁,自动转换sleep方法


def task1():
    for i in range(3):
        print("A", i)
        time.sleep(0.3)


def task2():
    for i in range(4):
        print("B", i)
        time.sleep(0.3)


def task3():
    for i in range(5):
        print("C", i)
        time.sleep(0.3)


if __name__ == '__main__':
    g1 = gevent.spawn(task1)
    g2 = gevent.spawn(task2)
    g3 = gevent.spawn(task3)
    g1.join()
    g2.join()
    g3.join()
