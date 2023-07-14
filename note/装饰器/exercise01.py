import time


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function = func(*args, **kwargs)
        execute_time = time.time() - start_time
        print("执行时间:", execute_time)
        return function
    return wrapper


@get_time
def func01():
    time.sleep(2)
    print("这是func01")


func01()
