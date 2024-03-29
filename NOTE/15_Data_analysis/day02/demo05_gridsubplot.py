"""
demo05_gridsubplot.py  网格式子图布局
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid Subplot', facecolor='lightgray')
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', 
		va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[:2, -1])
mp.text(0.5, 0.5, 2, ha='center', 
		va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, 3, ha='center', 
		va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, 4, ha='center', 
		va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.subplot(gs[-1, 1:])
mp.text(0.5, 0.5, 5, ha='center', 
		va='center', size=36, alpha=0.7)
mp.xticks([])
mp.yticks([])

mp.tight_layout()
mp.show()




