import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8080))

request_line = "GET/HTTP/1.1\r\n"
request_header = "Host: 127.0.0.1\r\n"
request_blank = "\r\n"
request_data = request_line + request_header + request_blank

client_socket.send(request_data.encode())
response = client_socket.recv(4098)
print(response.decode("utf-8"))

client_socket.close()
