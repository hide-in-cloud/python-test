import os
from multiprocessing import Process
from time import sleep

'''
process = Process(target=函数, name=进程名称, args=(给函数传的参数))
process 对象
对象调用的方法：
process.start()     启动进程并执行任务
process.run()       执行任务但没有启动进程
process.terminate() 终止进程
'''
'''
进程里的全局变量不能共享
'''

m = 100


def task1(second):
    global m
    while True:
        m += 1
        sleep(second)
        # os.getpid()获取当前进程id     os.getppid()获取父进程id
        print("这是任务1...m=", m, os.getpid(), "---", os.getppid())


def task2(second):
    global m
    while True:
        m += 1
        sleep(second)
        # os.getpid()获取当前进程id     os.getppid()获取父进程id
        print("这是任务2...m=", m, os.getpid(), "---", os.getppid())


if __name__ == '__main__':
    print(os.getpid())
    p1 = Process(target=task1, name="任务1", args=(1,))
    p1.start()
    print(p1.name)
    p2 = Process(target=task2, name="任务2", args=(2,))
    p2.start()
    print(p2.name)
    m = 0
    while True:
        sleep(0.5)
        print("main_m=", m)
        if m == 50:
            p1.terminate()
            p2.terminate()
            break
        else:
            m += 1

    print("----------")
