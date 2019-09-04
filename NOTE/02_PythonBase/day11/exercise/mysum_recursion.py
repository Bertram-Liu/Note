# 练习:
#   用递归的方式求和
#     def mysum_recursion(n):
#         ...
    
#     print(mysum_recursion(100))  # 5050



# def mysum_recursion(n):
#     if n == 1:
#         return 1
#     r = n + mysum_recursion(n - 1)
#     return r

def mysum_recursion(n):
    if n == 1:
        return 1
    return n + mysum_recursion(n - 1)

print(mysum_recursion(100))  # 5050