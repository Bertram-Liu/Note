#   写一个公式计算器的解释执行器
#   已知有如下一些函数:
#     def myadd(x, y):
#         return x + y
#     def mysub(x, y):
#         return x - y
#     def mymul(x, y)
#         return x * y
#   再自己写一个函数
#     def get_func(s):
#         ... # 此处自己实现
#     此函数传入一个字符串"加" 或 "+" 则返回myadd函数
#     此函数传入一个字符串"乘" 或 "*" 则返回mymul函数
#   在程序主函数中的程序如下:
#     def main():
#         while True:
#             s = input("请输入计算公式:")  # 10 加 20
#             L = s.split()  # L = ['10', '加', '20']
#             a = int(L[0])
#             b = int(L[2])
#             fn = get_func(L[1])
#             print("结果是:", fn(a, b))  # 结果是: 30
#     main()






def get_func(s):
    def myadd(x, y):
        return x + y

    def mysub(x, y):
        return x - y

    def mymul(x, y):
        return x * y

    if s == '加' or s == '+':
        return myadd
    elif s == '减' or s == '-':
        return mysub
    elif s in ('乘', '*'):
        return mymul

def main():
    while True:
        s = input("请输入计算公式:")  # 10 加 20
        L = s.split()  # L = ['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30
main()