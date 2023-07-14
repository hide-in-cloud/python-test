import pprint


def write_a_variable():
    cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]  # 创建一个变量
    print(pprint.pformat(cats))
    fileObj = open('myCats.py', 'w')  # 打开一个写入方式的py脚本
    fileObj.write('cats = ' + pprint.pformat(cats) + '\n')  # 写入变量
    fileObj.close()


def load_variable():
    import myCats
    cats = myCats.cats
    print(cats[0])


if __name__ == '__main__':
    load_variable()
