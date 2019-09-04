#   1. 写一个程序,以电子时钟的格式打印时间
#       格式为:
#         HH:MM:SS


import time

def show_time():
    # 在此处显示时间
    while True:
        # 取出本地时间
        t = time.localtime()
        # 显示时间
        # print("%02d:%02d:%02d" % (t[3], t[4], t[5]), end='\r')
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        time.sleep(1)

show_time()