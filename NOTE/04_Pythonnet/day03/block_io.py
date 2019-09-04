from socket import * 
from time import sleep,ctime  

sockfd = socket()
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)

# 设置非阻塞状态
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(6)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
    except timeout:
        print('time out .....')
    else:
        print("Connect from",addr)
        data = connfd.recv(1024)
        print(data)
