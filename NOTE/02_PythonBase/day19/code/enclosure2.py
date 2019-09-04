# enclosure.py

class A:
    def __init__(self, v):
        self.__money = v  # 私有属性

    def buy(self, obj, m):
        self.__money -= m
        print('买', obj, '花了', m, '元,剩余', 
        self.__money, '元')
        # 调用自己的私有方法
        self.__m()

    def __m(self):
        print("这是A类对象的私有实例方法")

a = A(1000)
a.buy('电纸书', 600)
# a.__m()   # 出错,私有实例方法不能在类的外部调用








