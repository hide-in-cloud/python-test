from collections import OrderedDict
'''按添加顺序记录键值对'''

languages = OrderedDict()

languages['1'] = 'python'
languages['2'] = 'c++'
languages['3'] = 'c'
languages['4'] = 'java'

for number, language in languages.items():
    print(number.title() + ' ' + language.title())
