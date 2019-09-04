from socket import * 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

# 接收名称
name = c.recv(1024).decode()
f = open(name,'wb')

while True:
    data = c.recv(1024)
    if data == b'##':
        break
    f.write(data)

c.send(b'Receive end')

f.close()
c.close()
s.close()