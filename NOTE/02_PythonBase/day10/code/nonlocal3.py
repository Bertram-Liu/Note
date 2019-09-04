# 当有两层或两层以上函数嵌套时,访问nonlocal变量只对最
# 近一层的变量进行操作

v = 100
def f1():
    v = 200
    print("f1开始时v=", v)  # 200
    
    def f2(v):
        nonlocal v  # 报错
        v = 300

    f2(999)
    print("f1结束时v=", v)  # 200

f1()
print("全局的v=", v)  # 100