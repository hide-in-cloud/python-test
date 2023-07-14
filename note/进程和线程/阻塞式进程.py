import random
import time
import os
from multiprocessing import Pool
'''
添加一个就执行一个任务，如果前一个任务未完成下一个任务就进不来
'''


def task(task_name):
    print("正在执行任务:", task_name)
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    print("完成任务:{}, 用时:{}, 进程id:{}".format(task_name, (end - start), os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)
    tasks_name = ['听音乐', '做饭', '吃饭', '打游戏', '看书', '弹吉他', '做作业']
    for t in tasks_name:
        pool.apply(task, args=(t,))  # apply方法
    pool.close()
    pool.join()  # 插队
