
# 此示例示意复合赋值算术运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        print("__mul__")
        L = self.data * rhs
        return MyList(L)
    
    def __imul__(self, rhs):
        print("__imul__")
        self.data *= rhs
        return self

L1 = MyList([1, 2, 3])
print(id(L1))
L1 *= 2
print(id(L1))
print("L1=", L1)



