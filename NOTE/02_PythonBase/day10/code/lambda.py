# lambda.py

# 此示例示意lambda表达式的语法和用法
# def myadd(x, y):
#     return x + y

# 以上函数可以改为为lambda实现
myadd = lambda x, y: x + y

print("20+30=", myadd(20, 30))  # 50
print("40+50=", myadd(40, 50))  # 90