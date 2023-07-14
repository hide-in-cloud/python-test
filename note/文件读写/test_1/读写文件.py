import json


def write_file():
    filename = 'words.txt'
    with open(filename, 'w') as fp:
        fp.write("I am a student.\nHello world!\nDo you know python?\n")


def append_file():
    filename = 'words.txt'
    with open(filename, 'a') as fp:
        fp.write("I love python.")


def read_file_1():
    filename = 'words.txt'
    with open(filename, 'r') as fp:
        contents = fp.read()  # 读取整个文件
        print(contents.rstrip())  # rstrip() 删除字符串末尾的空白


def read_file_2():
    filename = 'words.txt'
    with open(filename, 'r') as fp:
        for line in fp:  # 逐行读取
            print(line.rstrip())


def read_file_3():
    filename = 'words.txt'
    with open(filename, 'r') as fp:
        lines = fp.readlines()  # 读取每一行，并存储在一个列表中
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string)


# write_file()
# append_file()
read_file_1()


def dump_json():
    filename = 'numbers.json'
    numbers = [2, 3, 5, 7, 11, 13]
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)


def load_json():
    filename = 'numbers.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
    print(numbers)


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


dump_json()
load_json()

greet_user()
