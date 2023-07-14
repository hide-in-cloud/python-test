"""
    词典服务端
"""
import time
from socket import *
from multiprocessing import Process
import signal
import sys
from 电子词典.mysql import Database

HOST = '0.0.0.0'
PORT = 8080
ADDR = (HOST, PORT)
db = Database(database="dict")


def do_register(client, msg):
    content = msg.split(" ")
    name = content[1]
    passwd = content[2]
    if db.insert_data(name, passwd):
        client.send(b'OK')
    else:
        client.send(b'Fail')


def do_login(client, msg):
    content = msg.split(" ")
    name = content[1]
    passwd = content[2]
    if db.login(name, passwd):
        client.send(b'OK')
    else:
        client.send(b'Fail')


def do_query(client, msg):
    data = msg.split(" ")
    name = data[1]
    word = data[2]
    # 插入历史记录
    db.insert_into_history(name, word)
    # 查询单词意思
    mean = db.query(word)
    if not mean:
        client.send("查无此单词".encode())
    else:
        msg = "%s : %s" % (word, mean)
        client.send(msg.encode())


def do_history(client, data):
    name = data.split(" ")[1]
    data = db.display_history(name)
    if not data:
        client.send(b'Fail')
        return
    else:
        client.send(b'OK')
    for item in data:
        msg = "%s  %-16s  %s" % item
        time.sleep(0.1)
        client.send(msg.encode())
    time.sleep(0.1)
    client.send(b'##')


# 接收客户端请求
def request(client):
    db.create_cursor()
    while True:
        data = client.recv(1024).decode("utf-8")
        print(client.getpeername(), ":", data)
        if not data or data[0] == "E":
            sys.exit()
        elif data[0] == "R":
            do_register(client, data)
        elif data[0] == "L":
            do_login(client, data)
        elif data[0] == "Q":
            do_query(client, data)
        elif data[0] == "H":
            do_history(client, data)


def main():
    server_s = socket()
    server_s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    server_s.bind(ADDR)
    server_s.listen(3)
    # 处理僵尸进程
    signal.signal(signal.SIGABRT, signal.SIG_IGN)
    # 循环等待客户端连接
    print("Listen the port 8080")
    while True:
        try:
            client_socket, client_addr = server_s.accept()
            print("有新客户端接入:%s" % str(client_addr))
        except KeyboardInterrupt:
            server_s.close()
            db.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        # 为客户端创建子进程
        p = Process(target=request, args=(client_socket,))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()