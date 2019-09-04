from select import select 
from socket import * 
import sys 
from time import ctime  

# 日志文件
f = open('log.txt','a')

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

rlist = [s,sys.stdin]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            rlist.append(c)
        elif r is sys.stdin:
            f.write("%s  %s"%(ctime(),r.readline()))
            f.flush()
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue 
            f.write("%s   %s\n"%(ctime(),data.decode()))
            f.flush()