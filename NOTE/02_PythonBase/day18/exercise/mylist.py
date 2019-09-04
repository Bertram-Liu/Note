# 思考:
#   list 类里只有append向末尾追加数据的方法,但没有向列表头部
#   添加元素的方法,试想能否为例表在不改变原有功能的基础上添加
#   一个insert_head(n) 方法来实现向头部插入数据?
#   即:
#     class MyList(list):
#         def insert_head(self, n):
#             ...
#     myl = MyList(range(3, 6))
#     print(myl)  # [3, 4, 5]
#     myl.insert_head(2)
#     print(myl)  # [2, 3, 4, 5]
#     myl.append(6)
#     print(myl)  # [2, 3, 4, 5, 6]


class MyList(list):
    def insert_head(self, n):
        # self[0:0] = [n]  # 用切片头插
        self.insert(0, n)  


myl = MyList(range(3, 6))
print(myl)  # [3, 4, 5]
myl.insert_head(2)
print(myl)  # [2, 3, 4, 5]
myl.append(6)
print(myl)  # [2, 3, 4, 5, 6]
