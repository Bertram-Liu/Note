from socketserver import * 

# 创建服务器类
class Server(ForkingMixIn,UDPServer):
    pass 

class Handle(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break 
            print(data)
            self.wfile.write(b'OK')

server = Server(('0.0.0.0',8888),Handle)
server.serve_forever()