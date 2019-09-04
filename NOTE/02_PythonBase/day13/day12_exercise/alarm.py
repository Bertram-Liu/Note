#   2. 编写一个闹钟程序,启动时设定时间,到时间后打印一句语:
#       时间到,然后退出程序


def alarm(h, m):
    '''h 代表小时
       m 代表分钟
    '''
    import time
    while True:
        t = time.localtime()
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        if h == t[3] and m == t[4]:
            print("时间到!!!")
            return
        time.sleep(1)

hour = int(input("请输入小时: "))
minute = int(input("请输入分钟: "))
alarm(hour, minute)

