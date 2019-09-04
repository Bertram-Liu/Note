"""
demo07_sort.py　排序
"""
import numpy as np

products = np.array(['Apple', 'Huawei', 'Mi',
                     'Oppo', 'Vivo'])
prices = [8888, 5555, 1999, 2999, 2999]
volumns = np.array([100, 400, 150, 300, 260])

indices = np.lexsort((-volumns, prices))
print(indices)





