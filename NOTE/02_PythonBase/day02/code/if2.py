# if2.py

# 输入一个数字,用程序来判断这个数是正数,负数还是零

num = int(input("请输入一个整数: "))

if num > 0:
    print("您输入的是正数!")
elif num < 0:
    print("您输入的是负数!")
else:
    print("您输入的是零!")

