from socket import * 

#创建套接字对象
s = socket()

# 对套接字设置端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

s.bind(('0.0.0.0',8888))
s.listen(3)

print(s.family) #地址类型
print(s.type) #套接字类型

print(s.getsockname()) # 获取绑定addr
print(s.fileno()) #文件描述符

c,addr = s.accept()
print(c.getpeername())  #获取c对应的客户端地址

c.recv(1024)

