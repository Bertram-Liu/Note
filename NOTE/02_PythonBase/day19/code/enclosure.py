# enclosure.py

class A:
    def __init__(self, v):
        self.__money = v  # 私有属性
        self.__aaa__ = 10000  # 此实例属性不是私有属性

    def buy(self, obj, m):
        self.__money -= m
        print('买', obj, '花了', m, '元,剩余', 
        self.__money, '元')

a = A(1000)
a.buy('电纸书', 600)
print(a.__aaa__)
# print(a.__money)  # 取值也会报错
# a.__money -= 10000
a.buy('耳机', 100)







