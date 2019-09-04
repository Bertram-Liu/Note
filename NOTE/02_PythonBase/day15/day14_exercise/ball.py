#   2. 一个球从100米高空落下,每次落地后反弹高度为原高度的一半,
#      再落下.
#       1) 写程序算出皮球在第10次落地后反弹多高
#       2) 打印出第10次反弹后共经历多少米路程

def get_last_height(height, times):
    '''
    height 代表起始高度
    times 代表弹跳的次数
    返回值为: 最终的高度
    '''
    for _ in range(times):
        height /= 2

    return height

print("100米反弹10次后的高度为:",
       get_last_height(100, 10))

def get_distance(height, times):
    s = 0
    for _ in range(times):
        # 计算下落的距离
        s += height
        # 计算反弹的高度
        height /= 2
        # 累加反弹的距离
        s += height
    return s

print("小球从100反弹10次后的总路程为:",
       get_distance(100, 10))


