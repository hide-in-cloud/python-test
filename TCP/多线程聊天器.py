import socket
import time
import threading


def request_handle(conn, address):
    """处理客户端发来的请求"""
    while True:
        try:
            # 接收数据
            data = conn.recv(1024).decode('utf-8')
        except Exception:
            print("客户端%s已断开" % str(address))
            break
        print("收到客户端%s发送的内容:%s" % (str(address), data))
        reply = input("回复%s:" % str(address)).strip()
        if not reply:
            break
        msg = time.strftime('%Y-%m-%d %X')
        msg1 = '[%s]:%s' % (msg, reply)
        conn.send(msg1.encode('utf-8'))
    # 关闭当前连接
    conn.close()


def server_running():
    # 创建一个tcp协议的套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置地址重用 ???
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 获取当前主机ip
    host = socket.gethostname()
    # 设置端口
    port = 9090
    # 绑定端口
    server_socket.bind((host, port))
    # 设置监为听模式，设置最大客户端连接数为128
    server_socket.listen(128)

    # 存放客户端地址的容器
    address_list = []

    while True:
        # client_address接收ip和端口号,是一个元组
        conn, address = server_socket.accept()
        print("有新客户端接入:%s" % str(address))

        # 每连接一个客户端就创建一个线程
        thread_recv = threading.Thread(target=request_handle, args=(conn, address))
        # 加入地址容器
        address_list.append(address)
        # 设置线程守护 ???
        thread_recv.setDaemon(True)
        # 启动线程
        thread_recv.start()


if __name__ == '__main__':
    server_running()
