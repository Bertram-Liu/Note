# len_overwrite.py

# 此示例示意在自定义的类内添加__len__方法和__abs__方法
# 能让自定义的类用内建函数len和abs进行操作
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        s = 'MyList(%s)' % self.data
        return s

    def __len__(self):
        '此方法必须返回整数'
        return len(self.data)

myl = MyList([1, -2, 3, -4])
myl2 = MyList()
print(myl)  # 内部会用str(myl) 转为字符串
print(myl2)  #
print(len(myl))  # 
print(len(myl2))
# myl3 = abs(myl)
# print("myl3=", myl3)  # MyList([1, 2, 3, 4])