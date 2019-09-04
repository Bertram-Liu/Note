# init_method.py

# 此示例示意初始化方法的定义方式和调用传参
class Car:
    '''小汽车类'''
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        # return [1, 2, 3]  # 初始化方法内不允许返回除None以外的其它对象
        self.model = m  # 型号
        print('初始化方法被调用:', c, b, m)

    def run(self, speed):
        print(self.color, '的', self.brand, 
        self.model, '正在以', speed, '公里/小时的速度行驶')


a4 = Car('红色', '奥迪', 'A4')
a4.run(233)

# t1 = Car()
