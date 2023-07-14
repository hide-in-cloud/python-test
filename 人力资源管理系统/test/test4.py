import time


def str_plus_one(str_number, length):
    """字符串数字 + 1"""
    if str_number is None:
        str_number = '0001'
    else:
        number = int(str_number)
        str_number = str(number + 1)
        while len(str_number) < length:
            str_number = '0' + str_number
    return str_number


ID = ('001', '002', '005', '010')
max_id = int(max(ID))
id = str(max_id + 1)
while len(id) < 3:
    id = '0' + id
print(id)
print(str_plus_one(max(ID), 3))

# 当前时间
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
#         '%s','%s',%d,'%s',%d,'%s',%f,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
