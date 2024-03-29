'''
dict project for AID
'''
from socket import * 
import pymysql
import os,sys
import signal
import time 

# 定义全局变量
if len(sys.argv) < 3:
    print('''Start app as:
        python3 dict_server.py  0.0.0.0 8000
    ''')
    sys.exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
DICT_TEXT = './dict.txt'

# 搭建网络连接
def main():
    # 连接数据库
    db = pymysql.connect('localhost','root',\
        '123456','dict')
    
    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c,db) # 处理客户端请求
            sys.exit()
        else:
            c.close()

# 子进程函数,处理请求
def do_child(c,db):
    while True:
        # 接收请求
        data = c.recv(1024).decode()
        # 打印请求
        print(c.getpeername(),':',data)
        if not data or data[0] == 'E':
            c.close()
            return
        elif data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)

def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]

    cursor = db.cursor()
    sql = "select * from user where name='%s'"%name 
    cursor.execute(sql)
    r = cursor.fetchone() 
    if r != None:
        c.send(b'EXISTS')
        return 
    
    # 插入用户
    sql = "insert into user (name,passwd) values \
        ('%s','%s')"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FAIL')

def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]

    cursor = db.cursor()
    sql = "select * from user where name='%s' and \
        passwd='%s'"%(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    else:
        c.send(b'OK')

main()
