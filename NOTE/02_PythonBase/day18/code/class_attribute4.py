# class_attribute.py


# 此示例示意类属性的创建和使用
# 实例方法和类方法都属于类的属性
class Car:
    total_count = 0  # 创建类属性,用来保存汽车的数量
    def __init__(self):
        self.__class__.total_count += 1
    def run(self):
        print("小汽车正在跑!!!")

c1 = Car()
print(Car.total_count)  # 1
c2 = Car()
c3 = Car()
print(Car.total_count)  # 3
c1.run()


