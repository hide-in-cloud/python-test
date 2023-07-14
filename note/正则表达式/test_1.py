#! python3
import re


def test_1():
    # re.compile()生成的是正则对象，单独使用没有任何意义，需要和findall(), search(), match(）搭配使用
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # 生成一个正则对象，可重复利用
    mo = phoneNumRegex.search('My number is 415-555-4242.')  # 传入原字符串，找到匹配后返回一个Match对象
    print('Phone number found:' + mo.group())


def test_2():
    """匹配每 3 位就有一个逗号的数字"""
    regex = re.compile(r'^\d{1,3}(,\d{3})*$')
    number = regex.search('1,215,334')
    if number:
        print(number.group())


def test_3():
    """匹配姓 Nakamoto 的完整姓名"""
    name = re.compile(r'[A-Z][a-z]*\sNakamoto').search('Alen Nakamoto')
    if name:
        print(name.group())


if __name__ == '__main__':
    test_3()

