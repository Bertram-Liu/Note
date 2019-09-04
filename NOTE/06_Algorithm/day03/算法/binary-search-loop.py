# 二分查找

# 循环实现
# 原始数据 value
# 待查找数据 key
def binary(value, key):
    # 左侧下标/右侧下标值
    left = 0
    right = len(value) -1

    # 存在有效数据时继续查找
    while(left <= right):
        # 中间元素下标
        middle = (left + right) // 2
        # 对比
        if value[middle] == key:
            # 成功
            return middle
        elif value[middle] > key:
            # 左侧继续查找
            # 左侧下标不变
            # 右侧下标变为中间元素的前一位
            right = middle -1
        else:
            # 右侧继续查找
            # 右侧下标不变
            # 左侧下标变为中间元素的后一位
            left = middle + 1

    # 失败
    return -1


if __name__ == "__main__":
    # 原始数据 value
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13]
    # 待查找数据 key
    key = 7
    # 二分查找
    res = binary(value, key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功:", res)
