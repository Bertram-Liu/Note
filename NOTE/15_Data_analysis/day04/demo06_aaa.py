"""
demo06_aaa.py  轴向汇总
"""
import numpy as np

data = np.arange(1, 13).reshape(3, 4)
print(data)

# 轴向汇总
def func(ary):
	return np.max(ary), np.mean(ary), \
		np.min(ary)

r = np.apply_along_axis(func, 1, data)
print(r)
r = np.apply_along_axis(func, 0, data)
print(r)
