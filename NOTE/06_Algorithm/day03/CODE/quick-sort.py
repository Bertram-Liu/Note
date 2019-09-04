# 快速排序

# 原始数据
# value = [100,50,30,70,60,78,66,88,99,80]
def quick(value):
    # 递归的退出条件
    if len(value) < 2:
        return value

    # 设置关键数据
    mark = value[0]
    # 找出所有比关键数据小的
    small = [x for x in value if x < mark]
    # 找出所有比关键数据大的
    big = [x for x in value if x > mark]
    # 找出所有比关键数据相等的
    equal = [x for x in value if x == mark]
    # 从小到大排序：小的在前，大的在后
    return quick(small) + equal + quick(big)



if __name__ == "__main__":
    # 原始数据
    value = [100,50,30,70,60,78,66,88,99,80]
    value = quick(value)
    print("排序后：", value)
