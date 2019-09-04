from socket import * 
from time import sleep 

# 目标地址
dest = ('172.40.91.255',9999) 

s = socket(AF_INET,SOCK_DGRAM) #数据报套接字

# 设置可以发送接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = '''
    ***********************
         2019 植树节
         等春，也等你
    ***********************
'''

while True:
    sleep(2)
    s.sendto(data.encode(),dest)




