fun1 = lambda a, b: a if a > b else b
print(fun1(10, 5))

students = [
    {'name': 'Tom', 'age': 19},
    {'name': 'Anny', 'age': 18},
    {'name': 'Jack', 'age': 20}
]

# 按name key对应的值进行升序排列
# key 只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
students.sort(key=lambda x: x['name'])
print(students)

# 降序
students.sort(key=lambda x: x['name'], reverse=True)
print(students)

list1 = [2, 4, 5, 6, 3, 7, 8]
result = map(lambda x: x + 2, list1)
print(list(result))
