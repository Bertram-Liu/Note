#   2. 试写一个myfilter函数,要求此函数与内建的filter函数的功能
#      一致
#     如:
#       def myfilter(...):
#           ...
#       for x in myfilter(lambda x: x%2==1, range(10)):
#           print(x)  # 1 3 5 7 9



def myfilter(fn, iterable):
    for x in iterable:
        if fn(x):
            yield x

for x in myfilter(lambda x: x%2==1, range(10)):
    print(x)  # 1 3 5 7 9
