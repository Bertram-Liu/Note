from socket import * 
import sys 

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 具体功能
class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        pass

# 网络连接
def main():
    sockfd = socket()

    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接失败",e)
        return 

    # 创建实例化对象处理文件
    ftp = FtpClient(sockfd)

    while True:
        print("\n========命令选项==========")
        print("***       list       ***")
        print("***     get file     ***")
        print("***     put file     ***")
        print("***       quit       ***")
        print("===========================")
    
        cmd = input("输入命令>>")
        if cmd.strip() == 'list':
            ftp.do_list()

main()

