#   定义一个'人'类
#     class Human:
#         def set_info(self, name, age, address='不详'):
#             '''此方法用来给人对象添加'姓名', '年龄',
#                '家庭住址'属性
#             '''
#             ... # 此处自己实现

#         def show_infos(self):
#             '此处显示此人self的信息'
#             ... # 此处自己实现
#     h1 = Human()
#     h1.set_info('小张', 20, '北京市东城区')
#     h2 = Human()
#     h2.set_info('小李', 18)
#     h1.show_infos()  # 小张 今年 20 岁,家庭住址: 北京市东城区
#     h1.show_infos()  # 小李 今年 18 岁,家庭住址: 不详




class Human:
    def set_info(self, name, age, address='不详'):
        '''此方法用来给人对象添加'姓名', '年龄',
            '家庭住址'属性
        '''
        self.name = name
        self.age = age
        self.address = address

    def show_infos(self):
        '此处显示此人self的信息'
        print(self.name, '今年', self.age, 
              '岁,家庭住址:', self.address)

h1 = Human()
h1.set_info('小张', 20, '北京市东城区')
h2 = Human()
h2.set_info('小李', 18)
h1.show_infos()  # 小张 今年 20 岁,家庭住址: 北京市东城区
h2.show_infos()  # 小李 今年 18 岁,家庭住址: 不详

