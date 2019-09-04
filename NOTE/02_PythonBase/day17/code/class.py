# class.py

# 此示例示意class语句的用法
class Dog:
    pass


dog1 = Dog()  # 创建一个Dog类的实例
print(id(dog1))  # dog1这个对象的内存地址

dog2 = Dog()  # 创建另一个Dog类的实例
print(id(dog2))

lst1 = list()
print(id(lst1))

lst2 = list()
print(id(lst2))
