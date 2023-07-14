# import socket
# import threading
#
#
# def send_mas():
#     while True:
#         msg = input("请输入您要发送的内容:")
#         s.sendto(msg.encode('utf-8'), ('0.0.0.0', 8080))
#         if msg == 'exit':
#             break
#
#
# def recv_msg():
#     while True:
#         data, addr = s.recvfrom(1024)
#         print("接收到了{}地址，{}端口的消息：{}".format(addr[0],addr[1],data.decode("utf-8")))
#
#
# if __name__ == '__main__':
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(('0.0.0.0', 9090))
#     t1 = threading.Thread(target=send_mas())
#     t1.start()
#     t2 = threading.Thread(target=recv_msg())
#     t2.start()
