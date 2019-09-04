# for_range.py

i = 6
for x in range(1, i):
    print('x=', x, 'i=', i)
    i -= 1

print('------------')

i = 6
r = range(1, i)
for x in r:
    print('x=', x, 'i=', i)
    i -= 1

# 请问打印结果是什么?  print函数被调用几次?
