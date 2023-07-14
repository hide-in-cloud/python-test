"""
    假设你有一个无聊的任务，要在一篇长的网页或文章中，找出所有电话号码和
邮件地址。如果手动翻页，可能需要查找很长时间。如果有一个程序，可以在剪贴
板的文本中查找电话号码和 E-mail 地址，那你就只要按一下 Ctrl-A 选择所有文本，
按下 Ctrl-C 将它复制到剪贴板，然后运行你的程序。它会用找到的电话号码和 E-mail
地址，替换掉剪贴板中的文本。
"""

"""
# 从剪贴板取得文本。
# 找出文本中所有的电话号码和 E-mail 地址
# 将它们粘贴到剪贴板
"""

# 使用 pyperclip 模块复制和粘贴字符串。
# 创建两个正则表达式，一个匹配电话号码，另一个匹配 E-mail 地址。
# 对两个正则表达式，找到所有的匹配，而不只是第一次匹配。
# 将匹配的字符串整理好格式，放在一个字符串中，用于粘贴。
# 如果文本中没有找到匹配，显示某种消息

# ! python3

import re, pyperclip


def find_phone_email():
    phoneRegex = re.compile(r"""(
        (\d{3}|\(\d{3}\))?       # 3个数字或括号中的3个数字
        (\s|-|\.)?               # 空格、短横或句点
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )""", re.VERBOSE)  # re.VERBOSE 作为第二个参数 可以忽略正则表达式字符串中的空白符和注释

    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # username
        @                       # @
        [a-zA-Z0-9.-]+          # 域名
        (\.[a-zA-Z]{2,4})       # dot-somthing
        )''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        # 将匹配的电话号码转换成标准格式
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addressed found.')


if __name__ == '__main__':
    text = '''155156-55658156
800-420-7240
415-863-9900
415-863-9950
soidofs@dsdgdfsfv
info@nostarch.com
media@nostarch.com
academic@nostarch.c
'''
    find_phone_email()
