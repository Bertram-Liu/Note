# raise.py

# 此示例示意用raise语句发送错误通知后进入异常流程,给调用者
# 传递信息

def f1():
    print("f1开始")
    raise ValueError("f1里的错误!!!")
    print("f1结束")

def f2():
    print("f2开始")
    try:
        f1()
    except ValueError as err:
        print("f1里发生了错误!, err=", err)
        raise  # 等同于raise err
    print("f1结束")

try:
    f2()
except ValueError as err:
    print("f2里发生了错误, err=", err)

print("程序结束")







