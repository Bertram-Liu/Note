
# 此示例示意 in / not in 运算符的重载

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __contains__(self, e):
        print('__contains__')
        return e in self.data
        # return True

L1 = MyList([1, -2, 3, -4, 5])
print(3 in L1)  # ???
print(3 not in L1)
print(100 in L1)
print(100 not in L1)


