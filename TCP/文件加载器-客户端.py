import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
client.connect((host, 8080))
file_name = input("请输入要下载的文件名:\n")
client.send(file_name.encode())
# 创建文件，准备接收内容
with open("C:/Users/86138/Desktop/"+file_name, 'wb') as file:
    while True:
        data = client.recv(1024)
        if data:
            file.write(data)
        else:
            break

client.close()
