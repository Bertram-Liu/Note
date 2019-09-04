"""
demo05_poly.py  多项式基本操作
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2 -1000*x + 1

# 求多项式函数的导函数
P = [4, 3, -1000, 1]
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P, xs)
mp.scatter(xs, ys, marker='o', color='red',
	zorder=3)

mp.plot(x, y)
mp.show()