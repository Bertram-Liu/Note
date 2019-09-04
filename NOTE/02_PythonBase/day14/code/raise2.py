# raise.py

# 此示例示意用raise语句发送错误通知后进入异常流程,给调用者
# 传递信息

def make_except():
    print("函数开始...")

    # raise ValueError
    error = ValueError("这是我故意制造的一个错误!!!")
    raise error

    print("函数结束!")

try:
    make_except()
    print("make_except返回")
except ValueError as err:
    print("收到make_except 抛出错误信息!")
    print('err=', err)

print("程序结束")







