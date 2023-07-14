# 1. 用生成器函数实现
# 2. 体会函数式编程的"封装"
# 3. 体会函数式编程的"继承"与"多态"

list01 = [43, 4, 5, 6, 7, 87, 32, 65]

"""
# 找出所有偶数
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item


# 找出所有大于10的数
def find02():
    for item in list01:
        if item > 10:
            yield item


# 找出所有10~50的数
def find03():
    for item in list01:
        if 10 < item < 50:
            yield item


# "封装"
def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def condition03(item):
    return 10 < item < 50


# "继承"
def find(func_condition):
    for item in list01:
        # "多态"
        if func_condition(item):
            yield item


for item in find(condition02):
    print(item)
"""

from note.函数式编程.common01.list_helper import *

for item in ListHelper.find_all(list01, lambda item: item > 10):
    print(item)
