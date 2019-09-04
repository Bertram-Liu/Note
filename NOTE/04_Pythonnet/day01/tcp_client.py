from socket import *

# 创建tcp套接字
sockfd = socket()

# 发起连接
server_addr = ('127.0.0.1',8800)
sockfd.connect(server_addr)

# 收发消息
while True:
    data = input(">>")
    sockfd.send(data.encode())
    if data == '##':
        break
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()