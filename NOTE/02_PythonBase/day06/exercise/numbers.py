# 练习:
#   写一个程序,让用户输入两个以上的正整数,当输入小于零的数时结束
#   输入(要求不允许输入重复的数)
#   1) 打印这些数的和
#   2) 打印这些数中的最大数
#   3) 打印这些数中的第二大的数
#   4) 删除最小的一个数

L = []
while True:
    x = int(input('请输入正整数: '))
    if x < 0:
        # 如果L的个数大于等于2,则允许退出,否则继承输入
        if len(L) >= 2:
            break
        else:
            print("您输入的数据个数太少,请继承输入")
            continue
    # 如果x在L中不存在,则允许添加,否则打印一个未添加提示
    if x not in L:
        L.append(x)  # 追加
    else:
        print(x, "已经存在,添加失败!")

print(L)
#   1) 打印这些数的和
print("和是:", sum(L))
#   2) 打印这些数中的最大数
print("最大数是:", max(L))
#   3) 打印这些数中的第二大的数
L2 = L.copy()  # 复制一个副本
L2.sort(reverse=True)
print("第二大的数是:", L2[1])
del L2  # 释放L2绑定的列表

#   4) 删除最小的一个数
L.remove(min(L))

print(L)  # 最终结果

