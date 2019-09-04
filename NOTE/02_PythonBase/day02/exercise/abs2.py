#   2. 写一个程序,输入一个数,用条件表达式计算这个数的绝对值
#      并打印出来

n = int(input("请输入一个数:"))

result = n if n >= 0 else -n

print(n, "的绝对值是:", result)

