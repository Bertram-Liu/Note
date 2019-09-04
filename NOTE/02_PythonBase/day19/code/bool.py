
# 此示例示意在自定义的类内添加__len__方法和__bool__方法
# 实现返回自定义的布尔值

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        s = 'MyList(%s)' % self.data
        return s

    # def __len__(self):
    #     '此方法必须返回整数'
    #     print("__len__被调用")
    #     return len(self.data)
    
    # def __bool__(self):
    #     print("__bool__被调用")
    #     return len(self.data) != 0

myl1 = MyList([1, -2, 3, -4])
myl2 = MyList()
print(bool(myl1))  # True/False???
print(bool(myl2))  # ???

if myl1:
    print("myl1为真值")
else:
    print("myl1为假值")

# for x in myl1:  # myl1 不是可迭代对象
#     print(x)

