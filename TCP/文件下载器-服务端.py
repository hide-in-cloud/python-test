import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server.bind((host, 8080))
server.listen(128)
while True:
    client_socket, client_address = server.accept()
    print("客户端地址:", client_address)
    file_name = client_socket.recv(1024).decode()
    print(file_name)
    try:
        with open(file_name, 'rb') as file:
            while True:
                data = file.read(1024)
                if data:
                    client_socket.send(data)
                else:
                    break
    except Exception as e:
        print("文件%s下载失败" % file_name)
    else:
        print("文件%s下载成功" % file_name)

    client_socket.close()

# server.close()
