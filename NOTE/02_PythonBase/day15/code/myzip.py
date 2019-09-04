# myzip.py

# 此示例示意自己定义生成器函数myzip来替代zip函数
# def myzip(*args):
def myzip(iter1, iter2):
    it1 = iter(iter1)  # 拿到iter1的迭代器
    it2 = iter(iter2)  # 拿到iter2的迭代器
    while True:
        try:
            x = next(it1)  # 取出元组的第一个元素
            y = next(it2)  # 取出第二个元素
            yield (x, y)
        except StopIteration:
            return


# def myzip(iter1, iter2):
#     it1 = iter(iter1)  # 拿到iter1的迭代器
#     it2 = iter(iter2)  # 拿到iter2的迭代器
#     while True:
#         x = next(it1)  # 取出元组的第一个元素
#         y = next(it2)  # 取出第二个元素
#         yield (x, y)

numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for t in myzip(numbers, names):
    print(t)  # (10086, '中国移动'), (10000, '中国电信')


