# coding=utf-8
'''
HTTP Server v2.0
* 多线程并发
* 基本的请求解析
* 非网页处理
* 类的封装
'''

from socket import *
from threading import Thread
import sys  

# 将http具体功能封装在类里
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        # 添加对象属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.create_socket()
        self.bind()
    
    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Http server listen port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print("Error",e)
                continue 
            
            # 创建线程
            clientThread = Thread(target = self.handle,\
                args = (connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    
    # 处理具体请求
    def handle(self,connfd):
        # 接收HTTP请求
        request = connfd.recv(4096)
        
        # 浏览器异常断开
        if not request:
            connfd.close()
            return 
        
        # request解析
        requestlines = request.splitlines()
        print(connfd.getpeername(),':',requestlines[0])

        # 获取请求内容
        getRequest = str(requestlines[0]).split(' ')[1]

        if getRequest=='/' or getRequest[-5:]=='.html':
            self.get_html(connfd,getRequest)
        else:
            self.get_data(connfd,getRequest)
    
    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + getRequest   
        
        try:
            f = open(filename)
        except IOError:
            # 没有找到网页
            responseHeadlers = 'HTTP/1.1 404 Not Found\r\n'
            responseHeadlers += '\r\n'
            responseBody = "Sorry,Not found the page."
        else:
            # 返回对应网页
            responseHeadlers = 'HTTP/1.1 200 OK\r\n'
            responseHeadlers += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHeadlers + responseBody
            connfd.send(response.encode())
          
    def get_data(self,connfd,getRequest):
        responseHeadlers = 'HTTP/1.1 200 OK\r\n'
        responseHeadlers += '\r\n'
        responseBody = "<h1>Waiting httpserver v3.0</h1>"
        response = responseHeadlers + responseBody
        connfd.send(response.encode())

if __name__ == "__main__":
    # 用户自己设定的内容
    server_addr = ('0.0.0.0',8000)
    # 用户提供自己要展现的网页
    static_dir = './static'

    # 创建服务器对象
    httpd = HTTPServer(server_addr,static_dir)
    # 启动服务
    httpd.serve_forever()
     