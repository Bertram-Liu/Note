# global.py


# 3. 不能先声明局部变量,再用global声明为全局变量,此做法不
#     附合规则

v = 100

def f1():
    v = 200
    print(v)
    global v  # 警告,且没有创建局部变量
    v += 300
    print(v)


f1()
print("v=", v)  # ????