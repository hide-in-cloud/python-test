#! python3
import re


def test_1():
    str1 = 'a77ab8bac999c'
    pattern = '7'
    result = re.match(pattern, str1)  # 从头开始匹配，不符合为None
    print("result = ", result)
    print("list1 = ", re.split('a', str1))  # 遇到a就分割
    result1 = re.search(r'[a-z][0-9]+[a-z]', str1)  # 只找匹配的第一个
    result2 = re.findall(r'[a-z][0-9]+[a-z]', str1)  # 匹配全部
    print("result1=", result1.group())
    print("result2=", result2)


def test_2():
    # (?P<name>re) 匹配 re表达式,并捕获文本到名称为 name 的组里
    def double(matched):
        """将匹配的数字乘于 2"""
        value = int(matched.group('value'))
        return str(value * 2)

    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))  # re.sub(pattern, replace, string原串)


def match_100(number):
    """
        匹配字符串数字0-100
    :param number:
    :return:该数字
    """
    result3 = re.match('([1-9]?[0-9]?|100)$', number)
    print("result3=", result3.group())


def match_email():
    """验证邮箱"""
    email = 'qq76848515@qq.com'
    result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)$', email)
    if result:
        print(result.group())
    else:
        print("No match!")
    result = re.sub('qq', '163', email)  # 字符串替换
    print(result)


def match_html():
    """匹配网页信息"""
    msg = '<html><h1>abc</h1></html>'
    # ()分组， \1 \2  引用
    result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msg)  # 分组
    print(result.group())
    print(result.group(3))  # 获取中间的内容


def match_url():
    html = '<a href="/html/gndy/dyzz/20210130/61022.html" class="ulink">2021年剧情《发掘/挖掘/考古夺宝》BD中英双字幕</a>'
    result = re.findall(r'<a href=\"(.*)\" class=\".*\">(.*)</a>', html)
    print("url = ", result[0][0])
    print("title = ", result[0][1])


def main():
    print("————————————————————————————————————————————————")
    print("(6).匹配html中的href")
    print("————————————————————————————————————————————————")
    match_url()


if __name__ == '__main__':
    main()
