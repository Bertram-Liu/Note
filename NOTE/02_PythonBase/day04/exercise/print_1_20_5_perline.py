#   3. 打印1~20的整数,每行打印5个,打印四行,如:
#      1 2 3 4 5
#      6 7 8 9 10
#      ...
#      提示: 可以将if语句嵌入到while语句中

i = 1
while i <= 20:
    print(i, end=' ')
    if i % 5 == 0:
        print()  # 换行
    i += 1





# i = 1
# while i <= 20:
#     print(i, end=' ')
#     if i == 5:
#         print()  # 换行
#     if i == 10:
#         print()
#     if i == 15:
#         print()
#     if i == 20:
#         print()
#     i += 1



