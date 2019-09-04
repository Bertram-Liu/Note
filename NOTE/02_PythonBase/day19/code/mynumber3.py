# mynumber3.py


class MyNumber:
    def __init__(self, v):
        self.data = v

    def __float__(self):
        '''此方法必须返回浮点数'''
        return float(self.data)


n1 = MyNumber('100')
f1 = float(n1)  # ???
print(f1)  # 100.0


