# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
数组的掩码操作
"""
import numpy as np

# 使用掩码从大数组中截取子集
a = np.arange(1, 100)
print(a[(a % 3 == 0) & (a % 7 == 0)])

# 使用掩码把数组中的元素重新排列
b = np.array(['A', 'B', 'C', 'D'])
mask = [3, 0, 2, 0, 0, 1, 3, 0, 1]
print(b[mask])
