# globals_locals.py


# 此示例示意globals() 函数 和 locals函数的作用
a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    # 此时有几个全局变量,有几个局部变量???
    print("locals()返回:", locals())
    print("-------------------------")
    print('globals() 返回:', globals())
    print(c)  # 100
    mydict = globals()
    print('全局的c=', mydict['c'])  # 3
    print(globals()['c'])  # 3

fn(100, 200)

print("程序结束")








