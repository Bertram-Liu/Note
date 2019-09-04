# 二分查找

# 递归调用
# 原始数据 value
# 待查找数据 key

def binary(value, key, left, right):
    # 递归退出条件
    if left > right:
        return -1
        
    # 找出中间值
    middle = (left + right) // 2
    # 对比数据
    if value[middle] == key:
        # 若相等查找成功
        return middle
    elif value[middle] > key:
        # 若中间值大于待查找值,则左侧继续查找
        # 查找范围缩小:左侧下标值不变,
        # 右侧下标值变为中间元素的前一位
        return binary(value, key, left, middle-1)
    else:
        # 若中间值小于待查找值,则右侧继续查找
        # 查找范围缩小: 右侧下标值不变
        # 左侧下标值变为中间元素的下一位
        return binary(value, key, middle+1, right)



if __name__ == "__main__":
    # 原始数据 value
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13]
    # 待查找数据 key
    key = 7
    # 二分查找
    res = binary(value, key, 0, len(value)-1)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功:", res)
