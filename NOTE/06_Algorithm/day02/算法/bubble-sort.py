# 冒泡排序

# 原始数据 value
# [180, 120, 150, 164, 185, 100, 175, 190, 165, 160]
def bubble(value):
    # 外层循环: 对应数据走访次数     
    for i in range(len(value) -1):
        # 初始化标记为False 
        flag = False

        # 内层循环: 对应走访时相邻数据对比次数
        for j in range(len(value) - 1 - i):
            # 对比数据
            if value[j] > value[j+1]:
                # 交换数据
                value[j+1], value[j] = value[j], value[j+1]
                # 若已经进行数据交换,则标志为True
                flag = True
        
        # 若当前走访数据时,未进行数据交换
        # 则证明剩余数据有序,无需继续走访数据
        if flag is False:
            break

    print("遍历次数:", i+1)


if __name__ == "__main__":
    # 原始数据
    value = [260, 100, 120, 150, 160, 164, 165, 175, 180, 185, 190]
    print("原始数据:", value)
    # 排序
    bubble(value)
    print("排序后:", value)