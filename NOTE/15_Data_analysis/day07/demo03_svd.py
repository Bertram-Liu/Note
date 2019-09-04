"""
demo03_svd.py  奇异值分解
"""
import numpy as np

M = np.mat('1 5 9; 6 8 1')
U, sv, V = np.linalg.svd(M, full_matrices=False)
print(U)
print(sv)
print(V)
sv[1:] = 0
print(U * np.diag(sv) * V)


