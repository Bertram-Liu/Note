# continue3.py

# 此示例示意用跳过奇数的方式打印10以内的偶数

for x in range(10):
    if x % 2 == 1:
        continue
    print(x)
