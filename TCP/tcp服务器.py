# ('10.8.224.160', 9090)
# ('127.0.0.1', 9090)
import socket
import time


# 创建套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置地址重用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
host = socket.gethostname()
port = 9090
# 绑定端口
server_socket.bind((host, port))
# 设置监听，让套接字由主动变为被动
server_socket.listen(128)

while True:
    # client_address接收ip和端口号
    client_socket, client_address = server_socket.accept()
    print("有新客户端接入:%s" % str(client_address))
    while True:
        try:
            # 接收数据
            data = client_socket.recv(1024).decode('utf-8')
        except Exception:
            print("客户端%s已断开" % str(client_address))
            break
        print("客户端发送内容:", data)
        reply = input("回复:").strip()
        if not reply:
            break
        msg = time.strftime('%Y-%m-%d %X')
        msg1 = '[%s]:%s' % (msg, reply)
        client_socket.send(msg1.encode('utf-8'))
    # 关闭当前连接
    client_socket.close()
