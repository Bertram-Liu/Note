
# 此示例示意 索引的取值和赋值 运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):
        print('i=', i)
        if type(i) is int:
            print('正在做索引操作')
        elif type(i) is slice:
            print("正在做切片操作")
            print("起始值:", i.start)
            print("终止值:", i.stop)
            print("步  长:", i.step)
        return self.data[i]

L1 = MyList([1, -2, 3, -4, 5])
L2 = L1[::2]  # L2.__getitem__( slice(None, None, 2))
print("L2=", L2)
x = L1[1]
print('x=', x)





