import random
import time
import os
from multiprocessing import Pool


def task(task_name):
    print("正在执行任务:", task_name)
    start = time.time()
    time.sleep(random.random())
    end = time.time()
    # print()
    return "完成任务:{}, 用时:{}, 进程id:{}".format(task_name, (end - start), os.getpid())


container = []
def callback_func(retu):
    '''回调函数'''
    container.append(retu)


if __name__ == '__main__':
    pool = Pool(5)
    tasks_name = ['听音乐', '做饭', '吃饭', '打游戏', '看书', '弹吉他', '做作业']
    for t in tasks_name:
        pool.apply_async(task, args=(t,), callback=callback_func)  # apply_async方法
    pool.close()
    pool.join()  # 插队

    for c in container:
        print(c)
