# try_except.py

import copy

def div_apple(n):
    print(n, "个苹果您想分给几个人?")
    s = input('请输入人数: ')
    cnt = int(s)   # 可能触发ValueError错误
    result = n / cnt # 可能触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果')

try:
    div_apple(10)
    print("分苹果结束")
except (ValueError, ZeroDivisionError):
    print("分苹果失败,苹果被收回!")
# except ValueError:
#     print("分苹果失败,苹果被收回!")
# except ZeroDivisionError:
#     print("分苹果失败,苹果被收回!")

print("程序结束")

