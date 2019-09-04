# inherit.py

# 此示例示意单继承的语法和用法
# 等同于class Human(object):
class Human:
    '''定义一个'人'类,用来描述人的行为'''
    def say(self, what):
        print("say:", what)
    
    def walk(self, distance):
        print("走了", distance, '公里')

class Student(Human):
    def study(self, subject):
        print("学习:", subject)

class Teacher(Student):
    def teach(self, language):
        print("教:", language)
    
h1 = Human()
h1.say('今天天气真好!')
h1.walk(5)
s1 = Student()
s1.walk(4)
s1.say("走的有点累")
s1.study('python')

t1 = Teacher()
t1.teach("面向对象")
t1.walk(6)
t1.say('晚上吃点啥好!')
t1.study('魔方')









