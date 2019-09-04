# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo04_cls.py   ndarray存储复合类型数据
"""
import numpy as np

data = [('zs', [90, 70, 88], 15),
        ('ls', [91, 71, 81], 16),
        ('ww', [92, 72, 82], 17)]

# 第一种设置dtype的方式
ary = np.array(data, dtype='U2, 3int32, int32')
print(ary, 'ww age:',  ary[2]['f1'])

# 若字段较多，则可以使用第二种设置dtype的方式
ary = np.array(
    data, dtype=[('name', 'str', 2),
                 ('scores', 'int32', 3),
                 ('age', 'int32', 1)])
print(ary, 'ww age:',  ary[2]['age'])

# 第三种设置dtype的方式
ary = np.array(
    data, dtype={
        'names': ['name', 'scores', 'age'],
        'formats': ['U2', '3int32', 'int32']})
print(ary, 'ls scores:', ary[1]['scores'])

# 测试日期数据类型 datetime64
print('-' * 45)
data = ['2011', '2011-01-02', '2012-01-01',
        '2012-02-01 10:10:10']
dates = np.array(data)
print(dates, dates.dtype)

# 精确到Day的datetime64类型
dates = dates.astype('M8[D]')
print(dates, dates.dtype)
print(dates[2] - dates[0])
