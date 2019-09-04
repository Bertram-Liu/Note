"""
demo04_svd.py   奇异之分解
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

img = sm.imread('../da_data/lily.jpg', True)
print(img.shape)  # 512*512 元素都是亮度值
#　特征值提取
eigvals, eigvecs = np.linalg.eig(img)
print(eigvals.shape, eigvals.dtype)
print(eigvecs.shape, eigvecs.dtype)
#　抹掉特征值与特征向量
eigvals[50:] = 0
img2 = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * \
        np.mat(eigvecs).I
#　奇异之分解
U, sv, V = np.linalg.svd(img)
sv[10:] = 0
img3 = np.mat(U) * np.mat(np.diag(sv)) * np.mat(V)

mp.figure('Image EIG')
mp.subplot(221)
mp.imshow(img, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(224)
mp.imshow(img3.real, cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(223)
mp.imshow(img2.real, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()



