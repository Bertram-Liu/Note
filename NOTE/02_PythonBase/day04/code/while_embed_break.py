# break 语句只能终止当前循环语句的执行,如果有循环嵌套时,不
#     会跳出嵌套的外重循环


j = 0
while j < 10:
    # print('1 2 3 4 5 .... 19 20 ')
    i = 1
    while i <= 20:
        print(i, end=' ')
        if i == 15:
            break
        i += 1
    print()  # 换行

    j += 1




