# global.py

v = 100

def f1():
    global v
    v = 200  # 想让此语句来操作全局作用域的变量,怎么办?

f1()
print("v=", v)  # ????