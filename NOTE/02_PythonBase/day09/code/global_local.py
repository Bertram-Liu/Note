# global_local.py

# 此示例示意局部变量和全局变量

a = 100  # 创建 全局变量a绑定100
b = 200
def fx(c):  # c是形参,c也是局部变量,当函数调用结束后,c将被销毁
    b = 999
    d = 400  # 创建局部变量绑定 400
    print(a, b, c, d)

fx(300)
print('a=', a)
print('b=', b)  # 200
# print(d)  # 出错
