# attribute.py

# 此示例示意实例属性的用法
class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds,
              '正在吃', food)
        self.last_food = food  # 让自己记住上次吃的是什么

    def food_info(self):
        '''此方法用来显示小狗上次吃过的食物信息'''
        try:
            print(self.color, '的', self.kinds,
                '上次吃的是', self.last_food)
        except AttributeError:
            print("发生属性错误,显示食物信息失败!!!")

dog1 = Dog()
dog1.kinds = '京巴'  # 创建实例属性
dog1.color = '白色'  # 创建color 实例属性
dog1.color = '黄色'  # 修改实例属性
# print(dog1.color, '的', dog1.kinds)
dog1.eat('狗粮')
dog1.food_info()


dog2 = Dog()
dog2.kinds = '哈士奇'
dog2.color = '灰白'
# dog2.eat('骨头')
dog2.food_info()
# print(dog2.color)