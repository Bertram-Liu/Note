
# 此示例示意 索引的取值和赋值 运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):
        print('i=', i)
        return self.data[i]

    def __setitem__(self, i, v):
        print('i=', i, 'v=', v)
        self.data[i] = v

L1 = MyList([1, -2, 3, -4, 5])
x = L1[1]  # 等同于 x = L1.__getitem__(1)
print('x=', x)
L1[1] = 999
print("L1=", L1)  # MyList([1, 999, 3, -4, 5])


