# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
数组的切片
"""
import numpy as np

a = np.arange(1, 10)
#    index:  0 1 2 3 4 5 6 7 8
print(a)  # [1 2 3 4 5 6 7 8 9]
print(a[:3])  # 1 2 3
print(a[3:6])   # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9

# 多维数组的切片

a = np.arange(1, 28).reshape(3, 3, 3)
print(a, a.shape)
print(a[:2, :2, :2])
