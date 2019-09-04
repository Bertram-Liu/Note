# 练习:
#   写一个类Bicycle类(自行车类), 有run方法,调用时显示骑行里程
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
# 　再写一个类EBicycle(电动自行车类), 在Bicycle类的基础上添加
#     电池电量volume属性，
#     有两个方法:
#       1.fill_charge(vol)  用来充电，vol为电量（度)
#       2. run(km) 方法每骑行10km 消耗电量1度，同时显示当前
#       　　电量，当电量耗尽时，则调用Bicycle的run方法（人力
#       　　骑行)
#     class EBicycle(Bicycle):
#         ... # 此处自己实现，逻辑要符合现实
#     b = EBicycle(5)  # 新买的电动车内有5度电
#     b.run(10)  # 电动骑行了10公里，还剩4度电
#     b.run(100)  # 电动骑行了40公里，还剩0度电，人力骑行60km
#     b.fill_charge(10)  # 电动自行车充电10度
#     b.run(50)  # 电动骑行了50公里，还剩5度电





class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, '公里')


class EBicycle(Bicycle):
    def __init__(self, vol):
        self.volume = vol  # 电量

    def fill_charge(self, vol):
        self.volume += vol
        print("已成功充电", vol, '度')

    def run(self, km):
        # 先算电动骑行最多能骑多少?
        e_km = min(self.volume * 10, km)  # 电动骑行的公里数
        # 计算耗电量
        self.volume -= e_km / 10
        if e_km > 0:
            print("电动骑行了", e_km, '公里,还剩',
                  self.volume, "度电")
        if km > e_km:  # 电量不够最终要行里程时,人力骑行
            super().run(km - e_km)

b = EBicycle(5)  # 新买的电动车内有5度电
b.run(10)  # 电动骑行了10公里，还剩4度电
b.run(100)  # 电动骑行了40公里，还剩0度电，人力骑行60km
b.fill_charge(10)  # 电动自行车充电10度
b.run(50)  # 电动骑行了50公里，还剩5度电
