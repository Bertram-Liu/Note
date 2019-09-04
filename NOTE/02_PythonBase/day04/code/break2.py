# break.py

flag = False  # flag 表示 当前循环是否是条件不满足退出

i = 1
while i <= 6:
    print("循环开始时 i=", i)

    if i == 3:
        break

    print("循环结束时 i=", i)
    i += 1
else:
    print("这是while语句中的else子句")
    flag = True

if flag == True:
    print("循环条件不满足退出")
else:
    print("因为内部调用了break退出")
print("程序结束")