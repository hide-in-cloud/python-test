import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
client_socket.connect((host, 9090))
while True:
    data = input(">>").strip()
    if not data:
        break
    client_socket.send(data.encode('utf-8'))
    msg = client_socket.recv(1024)
    if not msg:
        break
    print(msg.decode('utf-8'))

client_socket.close()
