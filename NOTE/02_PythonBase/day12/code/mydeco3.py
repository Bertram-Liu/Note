# mydeco3.py

# 此示例示意用装饰器的语法来改变银行业务的需求

# 以下是小钱写的装饰器
def privileged_check(fn):
    def fx(n, x):
        print("正在验证权限...")
        fn(n, x)
    return fx

def send_message(fn):
    def fy(n, x):
        fn(n, x)
        print("正在发短信息给", n, '...')
    return fy

# -------- 以下是魏老师的写的程序--------
@privileged_check
def savemoney(name, x):
    print(name, '存钱', x, '元')

@send_message
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

# ---------以下是调用者小张写的程序--------
savemoney("小王", 200)
savemoney("小赵", 400)
withdraw("小李", 500)

