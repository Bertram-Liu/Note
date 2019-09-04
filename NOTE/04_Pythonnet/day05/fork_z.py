import os,sys 
from time import sleep 

pid = os.fork()

if pid == 0:
    print("Child PID:",os.getpid())
    sys.exit("子进程 。。。挂了")
else:
    while True:
        sleep(2)
        print("目送.........")

