# instance_method.py


class Dog:
    '''这是一种小动物类的定义
    这种动物是犬类,此类用于创建各种各样的小狗'''
    def eat(self, food):
        '''此方法用来描述小狗吃东西的行为'''
        print("ID为", id(self), '的小狗正在吃', food)
    
    def sleep(self, hour):
        print('小狗睡了', hour, '小时')
    
    def play(self, obj):
        print('小狗正在玩', obj)

dog1 = Dog()
dog1.eat('骨头')
dog1.sleep(1)
dog1.play('球')

dog2 = Dog()
dog2.eat('饺子')
dog2.play('飞盘')
dog2.sleep(3)

# 以下用类名.方法名来调用实例方法
Dog.eat(dog2, '狗粮')  # dog2.eat('狗粮')
