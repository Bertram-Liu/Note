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
    # def __init__(self, iterable=()):
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            self.data = iterable

    def __repr__(self):
        return "MyList(%s)" % str(self.data)

    def myextend(self, t):
        self.data += t


L1 = MyList()
L2 = MyList()
L1.myextend( (1, 2, 3, 4) )
print('L1=', L1)  # ????
print('L2=', L2)  # ????






# L1 = MyList([1, 2, 3])
# L2 = MyList([4, 5, 6])

# L3 = L1 + L2
# print(L3)  # MyList([1, 2, 3, 4, 5, 6])
# L4 = L2 + L1
# print(L4)  # MyList([4, 5, 6, 1, 2, 3])



