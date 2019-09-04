from threading import Thread 
from time import sleep 

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target = fun,name = 'Tarena')

# 设置daemon属性
t.setDaemon(True)
print('Daemon:',t.isDaemon())

t.start()

# 线程名称
print("Thread name:",t.name)
t.setName("Tedu")
print("Thread name:",t.getName())

# 线程是否在生命周期
print("is alive:",t.is_alive())



