# 练习:
#   自己写一个与enumerate功能相同的生成器函数myenumerate
#   如:
#     def myenumerate(...):
#         ...
    
#     names = ['中国移动', '中国电信', '中国联通']
#     for t in myenumerate(names):
#         print(t)  # (0, '中国移动'), (1, '中国电信), (...)

#     for t in myenumerate(names, 100):
#         print(t)  # (100, '中国移动'), (101, '中国电信), (...)



# 方法1
# def myenumerate(iterable, start=0):
#     it = iter(iterable)
#     while True:
#         try:
#             x = next(it)
#         except StopIteration:
#             return
#         yield (start, x)
#         start += 1

# 方法2
def myenumerate(iterable, start=0):
    for x in iterable:
        yield (start, x)
        start += 1

names = ['中国移动', '中国电信', '中国联通']
for t in myenumerate(names):
    print(t)  # (0, '中国移动'), (1, '中国电信), (...)

for t in myenumerate(names, 100):
    print(t)  # (100, '中国移动'), (101, '中国电信), (...)
