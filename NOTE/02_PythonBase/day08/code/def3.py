# 6. 函数有自己的名字空间,在函数外部不可以访问函数内部的变量
#    在函数内部可以访问函数外部的变量(但只能取值,不能赋值)

def myadd():
    x = 999
    he = x + y
    print(he)


x = 100
y = 200
myadd()

print(x)  # ????


