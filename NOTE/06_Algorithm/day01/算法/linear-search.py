# 顺序查找

# 原始数据value
# 待查找内容key
# [2, 5, 7, 1, 4, 13, 12, 9, 6, 10, 8, 11, 3]
def linear(value, key):
    for i in range(len(value)):
        if value[i] == key:
            # 查找成功
            return i
    else:
        # 查找失败
        return -1


if __name__ == "__main__":
    # 原始数据value
    value = [2, 5, 7, 1, 4, 13, 12, 9, 6, 10, 8, 11, 3] 
    # 待查找内容key
    key = 6
    
    # 调用查找函数
    res = linear(value, key)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功:",res)

    print((0+11) // 2)
    print((3+4) // 2)