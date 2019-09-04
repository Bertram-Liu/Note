from select import * 
from socket import *

# 创建关注IO 
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

# 创建poll对象
p = poll()

# 建立查找字典
fdmap = {s.fileno():s}

# 关注套接字
p.register(s,POLLIN|POLLERR)

# 循环监控关注IO
while True:
    events = p.poll() #阻塞等待IO发生
    # 遍历列表处理IO
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 注册新的IO
            p.register(c,POLLIN|POLLERR)
            fdmap[c.fileno()] = c 
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)  #取消关注
                fdmap[fd].close()
                del fdmap[fd]  #从字典删除
                continue
            print(data.decode())
            fdmap[fd].send(b'OK')

        
        



        

