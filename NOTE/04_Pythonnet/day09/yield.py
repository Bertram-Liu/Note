def fun():
    print("启动生成器")
    yield 1
    print("生成器完成")

# 生成器函数
g = fun()

print(next(g))
print(next(g))
