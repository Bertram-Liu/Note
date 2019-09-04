
# 此示例示意反向算术运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        L = self.data * rhs
        return MyList(L)

    def __rmul__(self, lhs):
        print("__rmul__")
        L = self.data * lhs
        return MyList(L)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])

L5 = L1 * 2  # L5 = L1.__mul__(2)
print("L5=", L5)  # MyList(1, 2, 3, 1, 2, 3)

L6 = 2 * L1  # L6 = L1.__rmul__(2) 
print("L6=", L6)



