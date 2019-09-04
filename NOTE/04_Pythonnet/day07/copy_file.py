from multiprocessing import Process 
import os 
from time import sleep 

filename = "./timg.jpg"
# 获取文件大小
size = os.path.getsize(filename)

# fr = open(filename,'rb')

# 复制上半部分
def top():
    n = size // 2 
    fr = open(filename,'rb')
    fw = open("top.jpg",'wb')

    while True:
        if n < 1024:
            fw.write(fr.read(n))
            break 
        fw.write(fr.read(1024))
        n -= 1024
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bottom.jpg','wb')
    fr.seek(size//2,0) 

    while True:
        data = fr.read(1024)
        if not data:
            break 
        fw.write(data)
    fr.close()
    fw.close()

t = Process(target=top)
b = Process(target=bot)
b.start()
t.start()
t.join()
b.join()
