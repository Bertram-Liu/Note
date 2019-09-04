from socketserver import * 

# 创建tcp多进程并发
# class Server(ForkingMixIn,TCPServer):
# class Server(ThreadingMixIn,TCPServer):
class Server(ThreadingTCPServer):
    pass 

# 具体请求处理类
class Handle(StreamRequestHandler):
    # 重写具体处理方法
    def handle(self):
        print("Connect from",self.client_address)
        while True:
            # self.request ==> accept返回的connfd
            data = self.request.recv(1024)
            if not data:
                break 
            print(data.decode())
            self.request.send(b'OK')

server_addr = ('0.0.0.0',8888)
# 创建服务器对象
server = Server(server_addr,Handle)
server.serve_forever() # 启动服务
