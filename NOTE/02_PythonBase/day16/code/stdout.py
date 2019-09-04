# stdout.py

# 此示例示意stdout文件的用法

import sys

sys.stdout.write("你好!!!")
sys.stdout.write("这是标准输入打印的文字")

print("这是print打印出来的文字!")
print("hello", file=sys.stdout)
sys.stdout.close()  # 一旦关闭这个文件.所有的屏幕输入将
                    # 不能使用
print('如果sys.stdout被并闭,这里将出现错误!!!')


