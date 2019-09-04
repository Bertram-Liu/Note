# stdin.py

# 此示例示意标准输入文件的用法:
import sys

s = input("请输入:")
print(s)

s = sys.stdin.readline()
print("s=", s)

