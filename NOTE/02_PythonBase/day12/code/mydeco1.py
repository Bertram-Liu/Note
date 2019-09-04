# mydeco1.py


# 此示例示意用装饰器来改变函数myfunc的功能
def mydeco(fn):
    def fx():
        print('+++++++++++')
        fn()
        print('-----------')
    return fx

def myfunc():
    print("myfunc被调用")

myfunc = mydeco(myfunc)  # ????

myfunc()
myfunc()
myfunc()


