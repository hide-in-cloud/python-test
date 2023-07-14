"""
    词典客户端

    功能：根据用户输入，发送请求，得到结果
    一级界面：注册，登录，退出
    二级界面：查单词，历史记录，注销
"""
import socket
import getpass
import sys

ADDR = ("127.0.0.1", 8080)
client_s = socket.socket()
client_s.connect(ADDR)


def query(name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        else:
            msg = "Q %s %s" % (name, word)
            client_s.send(msg.encode())
            data = client_s.recv(1024).decode()  # 查询结果
            print(data)


def history(name):
    msg = "H %s" % name
    client_s.send(msg.encode())
    data = client_s.recv(128).decode()
    if data == "OK":
        while True:
            data = client_s.recv(128).decode()
            if data == "##":
                break
            print(data)
    else:
        print("没有查询的历史记录")


def login(name):
    """
        二级界面
    :return:
    """
    while True:
        print("""
        =======================Query=====================
        1. 查单词             2. 历史记录            3. 注销
        =================================================
        """)
        cmd = input("输入选项:")
        if cmd == "1":
            query(name)
        elif cmd == "2":
            history(name)
        elif cmd == "3":
            return
        else:
            print("请输入正确的选项")


def do_register():
    while True:
        name = input("User name:")
        passwd = input("Password:")
        passwd2 = input("Again:")
        if " " in name or " " in passwd:
            print("用户名或密码不能有空格")
            continue
        if passwd != passwd2:
            print("两次密码不一致")
            continue
        msg = "R %s %s" % (name, passwd)
        client_s.send(msg.encode())
        data = client_s.recv(128).decode("utf-8")
        if data == "OK":
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return


def do_login():
    name = input("User:")
    passwd = input("Password:")
    msg = "L %s %s" % (name, passwd)
    client_s.send(msg.encode())
    data = client_s.recv(128).decode("utf-8")
    if data == "OK":
        print("登录成功")
        login(name)
    else:
        print("登录失败")


def main():
    while True:
        print("""
        =======================Welcome===================
        1. 注册               2. 登录              3. 退出
        =================================================
        """)
        cmd = input("输入选项:")
        if cmd == "1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            client_s.send(b'E')
            sys.exit("谢谢您的使用")
        else:
            print("请输入正确的选项")


if __name__ == '__main__':
    main()
