# mynumber.py

# 此示例示意在自定义的类内添加相应的方法,让自定义的类创建的实例
# 能够使用内建函数进行相应的操作

class MyNumber:
    def __init__(self, v):
        self.data = v

    # def __str__(self):
    #     print("__str__方法被调用")
    #     s = '数字:' + str(self.data)
    #     return s

    def __repr__(self):
        '''此方法必须返回能让eval执行自字符串'''
        s = 'MyNumber(%d)' % self.data
        return s

n1 = MyNumber(100)
print("repr(n1)=", repr(n1))
print("str(n1) =", str(n1))
