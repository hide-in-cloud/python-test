"""
    测试函数式编程查找列表中符合某个条件的单个元素
"""
from note.函数式编程.common01.list_helper import *


class SkillData:
    def __init__(self, id, name, damage, duration):
        self.id = id
        self.name = name
        self.damage = damage
        self.duration = duration

    def __str__(self):
        return "技能数据:%d,%s,%d,%d" % (self.id, self.name, self.damage, self.duration)


list_skill = [
    SkillData(102, "乾坤大挪移", 5, 10),
    SkillData(101, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

"""
# 查找名称为"葵花宝典"的技能
def search01():
    for item in list_skill:
        if item.name == "葵花宝典":
            return item


# 查找编号是101 的技能
def search02():
    for item in list_skill:
        if item.id == 101:
            return item


# 查找持续时间大于0的技能
def search03():
    for item in list_skill:
        if item.duration > 0:
            return item
"""

# def condition01(item):
#     return item.name == "葵花宝典"
#
#
# def condition02(item):
#     return item.id == 101
#
#
# def condition03(item):
#     return item.duration > 0

"""
def search(func_condition):
    for item in list_skill:
        if func_condition(item):
            return item


skill = search(condition03)
skill.show_data()
"""

# result = ListHelper.search(list_skill, condition01)
# result.show_data()

result = ListHelper.search(list_skill, lambda item: item.name == "葵花宝典")
print(result)
result = ListHelper.search(list_skill, lambda item: item.id == 101)
print(result)
result = ListHelper.search(list_skill, lambda item: item.duration > 0)
print(result)


# def get_count(func_condition):
#     count = 0
#     for item in list_skill:
#         if func_condition(item):
#             count += 1
#     return count


result = ListHelper.get_count(list_skill, lambda item: len(item.name) > 4)
print(result)
result = ListHelper.get_count(list_skill, lambda item: item.duration <= 5)
print(result)
