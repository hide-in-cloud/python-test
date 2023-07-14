from miniWeb服务器.application import urls
from miniWeb服务器.application import funs


def parse_request(request_data):
    """解析请求,获取访问路径"""
    request_text = request_data.decode('utf-8')
    request_line = request_text.splitlines()[0]  # 请求协议的第一行
    file_path = request_line.split(' ')[1]  # 第一行用空格分割,截取其中的路径
    # 设置默认首页
    if file_path == "/":
        file_path = "/index.html"
    return file_path


def create_http_response(status, response_body):
    """获取响应内容"""
    # 响应行
    response_line = "HTTP/1.1 %s\r\n" % status
    # 响应头
    response_header = "Server:Python20WS/2.1\r\n"
    # response_header += "Content-Type: text/html; charset=UTF-8\r\n"
    # 响应空行
    response_blank = "\r\n"
    # 拼接
    response_data = (response_line + response_header + response_blank).encode() + response_body
    return response_data


def application(current_dir, request_data):
    """响应请求"""
    file_path = parse_request(request_data)
    resource_path = current_dir + file_path
    response_data = ""

    if file_path.endswith(".py"):
        if file_path in urls.route_dict:
            func = urls.route_dict[file_path]
            response_body = func()
            response_data = create_http_response("200 OK", response_body.encode())
        else:
            response_body = "404 Error!\n"
            response_data = create_http_response("404 Not Found", response_body.encode())
    else:
        try:
            with open(resource_path, "rb") as file:
                # 响应主体
                response_body = file.read()
            response_data = create_http_response("200 OK", response_body)
        except Exception as e:
            response_body = "Error!\n%s" % str(e)
            response_body = response_body.encode()
            response_data = create_http_response("404 Not Found", response_body)

    return response_data
