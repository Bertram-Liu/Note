# slots_list.py

# 此示例示意类的 __slots__属性的作用
class Human:
    # 限制Human类型的对象只能有name和age实例属性
    __slots__ = ['name', 'age']
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def show_info(self):
        print(self.name, '今年', self.age, '岁')

h1 = Human('Tarena', 17)
h1.show_info()  # Tarena 今年 17 岁
# h1.Age = 18  # 报错,不允许添加此Age属性
h1.show_info()  # Tarena 今年 17 岁

