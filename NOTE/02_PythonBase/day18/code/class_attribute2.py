# class_attribute.py


# 此示例示意类属性的创建和使用
class Car:
    total_count = 0  # 创建类属性,用来保存汽车的数量


c1 = Car()  # 创建一个实例(对象)

# 类属性可以通过此类的实例直接访问(取值不能赋值)
print(c1.total_count)  # 0 取值
c1.total_count = 999  # 此赋值会创建实例属性而不是修改类属性
print(c1.total_count)  # 999
print(Car.total_count)  # 0  # 类属性不会被修改

