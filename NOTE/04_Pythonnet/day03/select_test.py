from select import select 
from socket import *
import sys 

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

rs,ws,xs = select([s,sys.stdin],[],[])

print(rs)

