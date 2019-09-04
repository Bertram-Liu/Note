from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# 选择接收端口
s.bind(('0.0.0.0',9999))

while True:
    msg,addr = s.recvfrom(1024)
    print(msg.decode())


