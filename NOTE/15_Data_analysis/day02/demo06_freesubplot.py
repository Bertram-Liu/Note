"""
demo06_freelayout.py 自由布局
"""
import matplotlib.pyplot as mp

mp.figure('FlowLayout', facecolor='lightgray')

mp.axes([0.1, 0.2, 0.5, 0.3])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.show()