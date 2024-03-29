
# 此示例示意一元运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        lst = [-x for x in self.data]
        return MyList(lst)

    def __pos__(self):
        return MyList([abs(x) for x in self.data])

L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1
print("L2=", L2)  # MyList([-1, 2, -3, 4, -5])

L3 = +L1
print("L3=", L3)  # MyList([1, 2, 3, 4, 5])


