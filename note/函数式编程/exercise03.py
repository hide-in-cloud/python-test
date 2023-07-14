from note.函数式编程.common01.list_helper import *


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.hp, self.atk, self.defense)


list_enemy = [
    Enemy("灭霸", 0, 200, 199),
    Enemy("成昆", 50, 5, 10),
    Enemy("小丑", 1, 66, 33),
    Enemy("阿兹尔", 100, 150, 90),
]

res = ListHelper.is_exist(list_enemy, lambda item: item.name == "灭霸")
print(res)

# res = ListHelper.sum(list_enemy, lambda item: item.hp)
# print(res)


# def get_max(func_handle):
#     max_value = list_enemy[0]
#     for i in range(1, len(list_enemy)):
#         if func_handle(list_enemy[i]) > func_handle(max_value):
#             max_value = list_enemy[i]
#     return max_value


# res = ListHelper.get_max(list_enemy, lambda item: item.atk)
# print(res)


# def mapped(func_handle):
#     for item in list_enemy:
#         yield func_handle(item)


# res = ListHelper.mapped(list_enemy, lambda item: item.name)
# for item in res:
#     print(item)


# def order_by(func_handle):
#     for i in range(len(list_enemy)):
#         for j in range(i+1, len(list_enemy)):
#             if func_handle(list_enemy[j]) < func_handle(list_enemy[i]):
#                 list_enemy[i], list_enemy[j] = list_enemy[j], list_enemy[i]


# ListHelper.order_by(list_enemy, lambda item: item.defense)
# for item in list_enemy:
#     print(item)

print(max(([1, 1, 1], [2, 2], [3, 3, 3, 3]), key=lambda item: len(item)))
