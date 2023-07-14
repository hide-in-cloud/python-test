import socket
from miniWeb服务器.application import app
import multiprocessing


class MyServer(object):
    def __init__(self, ip, port):
        # 创建套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        server_socket.bind((ip, port))
        # 设置监听，让套接字由主动变为被动
        server_socket.listen(128)

        self.server_socket = server_socket

    def start(self):
        print("web服务器已启动...")
        while True:
            # client_address接收ip和端口号
            client_socket, client_address = self.server_socket.accept()
            print("有新客户端接入,%s" % str(client_address))
            # 创建线程
            p1 = multiprocessing.Process(target=self.request_handler, args=(client_socket, client_address))
            p1.daemon = True
            p1.start()
            # 子线程会拷贝一份client，需要再次关闭client
            client_socket.close()

    def request_handler(self, client_socket, client_address):
        request_data = client_socket.recv(1024)
        if not request_data:
            print("客户端%s已断开" % str(client_address))
            client_socket.close()
            return
        response_data = app.application("/pythonHello/miniWeb服务器/static", request_data)

        client_socket.send(response_data)
        client_socket.close()


def main():
    ###############################################
    # 命令行运行
    # if len(sys.argv) != 2:
    #     print("参数格式错误!")
    #     return
    # if not sys.argv[1].isdigit():
    #     print("端口号非数字类型")
    #     return
    # port = int(sys.argv[1])
    ###############################################
    port = 8080
    server = MyServer('', port)
    server.start()


if __name__ == '__main__':
    main()
