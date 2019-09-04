# myiterable.py


# 此示例示意将自定义的类创建的对象变为可迭代对象并能用
# for语句进行遍历

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        s = 'MyList(%s)' % self.data
        return s
    def __iter__(self):
        '''此方法会将MyList对象作为可迭代对象,此方法
        要求必须返回迭代器'''
        myit = MyListIterator(self.data)  # 创建迭代器
        return myit

class MyListIterator:
    '''此类的对象将作为迭代器来访问MyList类型的对象'''
    def __init__(self, lst):
        self.data = lst
        self.cur_index = 0  # 用记录当前访问位置的索引
    def __next__(self):
        # 如果数据已经获取完毕,抛出StopIteration异常
        if self.cur_index >= len(self.data):
            raise StopIteration
        r = self.data[self.cur_index]
        self.cur_index += 1
        return r
        # return 999

myl1 = MyList([1, -2, 3, -4])
it = iter(myl1)  # it = myl1.__iter__()
while True:
    try:
        x = next(it)  # it.__next__()
        print(x)
        import time
        time.sleep(1)
    except StopIteration:
        break
print('-------------------')
for x in myl1:
    print(x)  # 打印: 1  -2  3  -4


