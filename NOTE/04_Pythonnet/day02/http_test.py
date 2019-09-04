from socket import *

# 创建套接字
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3) 

# 接收浏览器请求
c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096)
print(data)

# 组织http响应格式
data = '''HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
'''
c.send(data.encode())

c.close()
s.close()
