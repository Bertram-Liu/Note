'''
ftp 文件服务器
fork server训练
socket使用
'''
from socket import *
import os,sys 
import signal

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
# 文件库目录
FILE_PATH = '/home/tarena/FTPSERVER/'

# 功能类
class FtpServer(object):
    pass 


# 循环接收请求
def do_requests(connfd):
    while True:
        data = connfd.recv(1024).decode()
        

# 网络通信 
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

    # 处理僵尸
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 8888...")

    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print('服务器异常:',e)
            continue 
        print("连接客户端:",addr)
        
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            sockfd.close()
            do_requests(connfd) # 处理请求
            os._exit(0)
        else:
            connfd.close()

main()





