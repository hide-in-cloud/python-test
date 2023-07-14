import socket


def request_handler(client_socket, client_address):
    request_data = client_socket.recv(1024)
    if not request_data:
        print("客户端%s已断开" % str(client_address))
        client_socket.close()
        return
    # 获取访问路径
    request_text = request_data.decode('utf-8')
    request_line = request_text.splitlines()[0]  # 请求协议的第一行
    path = request_line.split(' ')[1]  # 第一行用空格分割,截取其中的路径
    # 设置默认首页
    if path == "/":
        path = "/index.html"

    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "Content-Type: text/plain; charset=UTF-8\r\n"
    # 响应空行
    response_blank = "\r\n"
    try:
        with open("/pythonHello/TCP"+path, "rb") as file:
            # 响应主体
            response_body = file.read()

    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_body = "Error!\n%s" % str(e)
        response_body = response_body.encode()
    # 拼接
    response_data = (response_line + response_header + response_blank).encode() + response_body

    client_socket.send(response_data)
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(("", 8080))
    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        print("有新客户端接入,%s" % str(client_address))
        request_handler(client_socket, client_address)


if __name__ == '__main__':
    main()
