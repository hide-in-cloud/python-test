import re


def test_3(string, delete_str=None):
    if delete_str is None:
        regex = re.compile(r'^\s*|\s*$')
    else:
        regex = re.compile(r'^{0}*|{0}*$'.format(delete_str))
    result = regex.sub('', string)
    return result


if __name__ == '__main__':
    inputStr1 = input('请输入原字符串:')
    inputStr2 = input('请输入要去除的字符:')
    if inputStr2 == '':
        print('去除后的字符串为:' + test_3(inputStr1))
    else:
        print('去除后的字符串为:' + test_3(inputStr1, inputStr2))
