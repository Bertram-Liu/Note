# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_attr.py   数组属性基本操作
"""
import numpy as np

# shape 维度
ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, ary.shape)
# 修改shape属性
ary.shape = (2, 3)
print(ary, ary.shape)
print('-' * 45)

# dtype 元素数据类型
ary = np.arange(6)
print(ary, '  dtype:', ary.dtype)
# ary.dtype = 'int64'
# print(ary, '  dtype:', ary.dtype)  # 不合理
ary = ary.astype('float32')
print(ary, '  dtype:', ary.dtype)
print('-' * 45)

# size 数组元素个数
ary.shape = (2, 3)
print(ary, ' size:', ary.size, ' len:', len(ary))

# 元素索引
ary = np.arange(1, 9)
ary.shape = (2, 2, 2)
print(ary)
print(ary[1])
print(ary[1][1][0])
print(ary[1, 1, 0])
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i, j, k], end=' ')
