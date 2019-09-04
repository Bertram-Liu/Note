import socket 

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET,\
    socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',8800))

# 设置监听
sockfd.listen(5)

# 等待客户端连接
print("Waiting for connect ...")
connfd,addr = sockfd.accept()
print("Connect from",addr)  #客户端地址

# 收发消息
while True:
    data = connfd.recv(1024)
    print("Receive message:",data.decode())
    if data.decode() == '##':
        break
    n = connfd.send(b'Thanks your message')
    print("Send %d bytes"%n)

# 关闭套接字
connfd.close()
sockfd.close()





