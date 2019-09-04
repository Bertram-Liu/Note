# 信号处理僵尸进程
import os 
import signal 

# 处理语句
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()

if pid == 0:
    print("Child process",os.getpid())
else:
    while True:
        pass 