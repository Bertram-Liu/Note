# 练习:
#   实现两个自定义列表相加
#     class MyList:
#         ... 此处自己实现
#     L1 = MyList([1, 2, 3])
#     L2 = MyList([4, 5, 6])
#     L3 = L1 + L2
#     print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#     L4 = L2 + L1
#     print(L4)  # MyList([4, 5, 6, 1, 2, 3])



class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        L = self.data + rhs.data
        return MyList(L)

    def __mul__(self, rhs):
        L = self.data * rhs
        return MyList(L)

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])

L5 = L1 * 2  # L5 = L1.__mul__(2)
print("L5=", L5)  # MyList(1, 2, 3, 1, 2, 3)
# 思考如下代码会怎么样？
L6 = 2 * L1  # L6 = 2.__mul__(L1)  # 报错
print("L6=", L6)



