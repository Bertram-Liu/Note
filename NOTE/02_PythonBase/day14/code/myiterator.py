# myiterator.py

# 此示例示意用迭代器来遍历列表

L = [2, 3, 5, 7]
it = iter(L)  # 让L提供迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
print("---------------")
L = [2, 3, 5, 7]
for x in L:
    print(x)



print("程序结束")
