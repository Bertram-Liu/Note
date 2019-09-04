from threading import Thread 
from time import sleep,ctime 

# 自定义线程类
class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={},\
        name="Thread-1"):
        super().__init__()
        self.target = target
        self.args = args 
        self.kwargs = kwargs
        self.name = name 
    
    def run(self):
        self.target(*self.args,**self.kwargs)

# ********************************
# 不要修改以下内容,根据以下内容,完成上面类的编写
# *******************************

# 测试函数,此函数只是例举,函数名称,参数名称和个数不定
def player(sec,song):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

# 类的使用
t = MyThread(target=player,args=(3,),\
    kwargs={'song':'凉凉'},name='AID')
t.start()
t.join()







