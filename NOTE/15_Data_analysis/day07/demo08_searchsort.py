"""
demo08_searchsort.py插入排序
"""
import numpy as np

#             0  1  2  3  4  5  6
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])
indices = np.searchsorted(a, b)
print(indices)

d = np.insert(a, indices, b)
print(d)