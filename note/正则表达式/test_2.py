import re


def test_1(password):
    """匹配强口令:长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字"""
    len_re = re.compile(r'.{8,}')
    num_re = re.compile(r'.*\d')
    low_re = re.compile(r'.*[a-z]')
    upp_re = re.compile(r'.*[A-Z]')
    if len_re.search(password) and num_re.search(password) and low_re.search(password) and upp_re.search(password):
        print(password + ' is a strong password')
        return True
    else:
        print("Your password is not enough strong")
        return False


def test_2(password):
    """匹配强口令:长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字"""
    passwordRegex = re.compile(r'''(
        (?=.{8,})                   # 8位以上
        (?=.*\d)                    # 至少一个数字
        (?=.*[a-z])                 # 至少一个小写字母
        (?=.*[A-Z])                 # 至少一个大写字母
        )''', re.VERBOSE)
    match = passwordRegex.match(password)
    if match:
        print(match)
        return True
    else:
        print("Your password is not enough strong")
        return False


if __name__ == '__main__':
    password = input('输入密码:')
    while not test_2(password):
        password = input('输入密码:')
