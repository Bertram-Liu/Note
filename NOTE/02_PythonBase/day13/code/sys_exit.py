

import sys
# break 语句  退出循环
# return 语句 退出当前函数
# sys.exit()  退出程序
print("程序开始")
def fx():
    print("函数开始")
    sys.exit()  # 退出程序
    print("函数结束")

fx()

print("程序结束")