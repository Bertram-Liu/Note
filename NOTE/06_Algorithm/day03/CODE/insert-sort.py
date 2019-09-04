# 插入排序

# 原始数据
# value = [100,50,30,70,60,78,66,88,99,80]
def insert(value):
    # 外层循环：对应遍历所有无序数据,取出当前无序数据
    # 从第一个无序数据开始：即第二个数据开始
    for i in range(1, len(value)):
        # 取出当前无序数据
        temp = value[i]
        # 存储将要插入数据的位置
        pos = i

        # 内层循环：对应从后扫描比较所有有序数据,找到数据插入位置
        # 开始位置：从最后一个有序数据开始，即当前无序数据的前一位
        # 结束位置：下标为０的位置，包含０
        # 从后向前：　-１
        for j in range(i-1, -1, -1):
            # 比较有序数据与取出数据
            if value[j] > temp:
                # 当前有序数据后移
                value[j+1] = value[j]
                # 更新数据插入位置
                # 对应当前有序数据
                pos = j# 最后对应在所有有序数据均大于取出数据的情况
            else:
                # 有序数据小于等于取出数据
                # 在当前数据的后一位置插入取出数据
                pos = j+1
                # 已经确认数据插入位置
                break

        # 确认数据位置后插入数据
        value[pos] = temp

if __name__ == "__main__":
    # 原始数据 
    value = [100,50,30,70,60,78,66,88,99,80]
    insert(value)
    print("排序后：", value)