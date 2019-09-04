# nonlocal.py

v = 100
def f1():
    v = 200
    print("f1开始时v=", v)  # 200
    
    def f2():
        nonlocal v
        v = 300
    f2()

    print("f1结束时v=", v)  # 300

f1()
print("全局的v=", v)  # 100