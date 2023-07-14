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