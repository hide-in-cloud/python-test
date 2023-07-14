import random

# 1. 列表推导式: 格式:[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if]
names = ['tom', 'lily', 'jack', 'bob', 'steven']
result = [name for name in names if len(name) > 3]  # 把符合条件的给到name
print(result)
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# (0~4的偶数, 0~9的奇数)
list1 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(list1)

dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 3000}
dict4 = {'name': 'lily', 'salary': 4000}
list2 = [dict1, dict2, dict3, dict4]
new_list = [employee['salary']+200 if employee['salary'] > 5000 else employee['salary']+500 for employee in list2]
print(new_list)

# 生成器
g = (x*3 for x in range(100))
print(g.__next__())  # 法1
print(next(g))       # 法2
print(g.__next__())

'''
排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))  # 不改变原来的排列顺序

print("\nHere is the original list again:")
print(cars)

cars.sort()  # 永久性地修改
print(cars)
'''


def count_digits():
    """升序输出所有不同的数字及其每个数字重复的次数"""
    a = []
    for i in range(1000):
        a.append(random.randint(20, 100))

    b = sorted(a)
    c = dict()
    for i in b:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    print(c)
