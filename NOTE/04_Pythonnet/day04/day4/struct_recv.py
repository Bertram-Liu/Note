from socket import *
import struct 

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 确定数据结构
st = struct.Struct('i16sf')

while True:
    data,addr = s.recvfrom(1024)
    data = st.unpack(data)  #解析数据
    print('id:',data[0])
    print('name:',data[1].decode())
    print('height:%.2f'%data[2])
s.close()