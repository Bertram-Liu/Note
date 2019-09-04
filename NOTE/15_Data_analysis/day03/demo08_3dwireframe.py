"""
demo08_3dwireframe.py  三维线框图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), 
				   np.linspace(-3, 3, n))
#  根据一个奇妙的公式算出每个坐标点的高度值z
z = (1 - x/2 + x**5 + y**3) * \
		np.exp(-x**2 - y**2)
# 绘制
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface')
ax3d = mp.gca(projection='3d')
ax3d.plot_wireframe(x, y, z, rstride=30, 
	cstride=30, cmap='jet', linewidth=1)
mp.show()














