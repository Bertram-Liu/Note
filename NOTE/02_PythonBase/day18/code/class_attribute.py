# class_attribute.py


# 此示例示意类属性的创建和使用
class Car:
    total_count = 0  # 创建类属性,用来保存汽车的数量


# 类属性,可以通过该类直接访问
print(Car.total_count)  # 0  # 取类属性的值

Car.total_count += 100  # 修改类属性

print(Car.total_count)  # 100
