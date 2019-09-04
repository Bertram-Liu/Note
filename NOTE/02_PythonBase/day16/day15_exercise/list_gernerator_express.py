#   1. 看下列函数的输出结果是什么? 为什么?
#     第一个程序:
#       L = [2, 3, 5, 7]
#       A = [x * 10 for x in L]
#       it = iter(A)
#       print(next(it))  # ????
#       L[1] = 333
#       print(next(it))  # ????
#     第二个程序:
#       L = [2, 3, 5, 7]
#       A = (x * 10 for x in L)
#       it = iter(A)
#       print(next(it))  # ????
#       L[1] = 333
#       print(next(it))  # ????



# 第一个程序:
L = [2, 3, 5, 7]
A = [x * 10 for x in L]
it = iter(A)
print(next(it))  # 20
L[1] = 333
print(next(it))  # 30

# 第二个程序:
L = [2, 3, 5, 7]
A = (x * 10 for x in L)  # 生成器是现用现生成,
it = iter(A)
print(next(it))  # 20
L[1] = 333
print(next(it))  # 3330 




