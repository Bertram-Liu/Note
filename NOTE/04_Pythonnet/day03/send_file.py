from socket import * 
import time

s = socket()
s.connect(('127.0.0.1',8888))

f = open('file.jpg','rb')

# 发送图片名称
name = input("name:")
s.send(name.encode())
time.sleep(0.1)

while True:
    data = f.read(1024)
    if not data:
        time.sleep(0.1)
        s.send(b'##')
        break
    s.send(data)

data = s.recv(1024).decode()
print(data)

f.close()
s.close()


