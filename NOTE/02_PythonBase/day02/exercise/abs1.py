#   1. 写一个程序,输入一个数,用if语句计算这个数的绝对值并打印出来

n = int(input("请输入一个数: "))

result = n  # 先用一个变量来记录输入的数
if result < 0:
    result = -result

print(n, "的绝对值是:", result)

