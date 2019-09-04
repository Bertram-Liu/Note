# function_as_args.py

# 此示例示意函数可以作为实参传递给另一个函数
def f1():
    print("f1被调用")

def f2():
    print("f2被调用")

def fx(fn):
    print(fn)  # <function f1 at 0xXXXXXXX>
    fn()  # 通过形参fn间接调用了fn绑定的函数

# fx(100)
fx(f1)
fx(f2)


