"""
demo07_locators.py  刻度定位器
"""
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()', 
			'mp.MultipleLocator(2)', 
			'mp.MaxNLocator(nbins=4)']


mp.figure('Locators', facecolor='lightgray')


for i, locator in enumerate(locators):
	mp.subplot(len(locators), 1, i+1)
	ax = mp.gca()
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	mp.ylim(-1, 1)
	mp.xlim(1, 10)
	ax.spines['bottom'].set_position(('data', 0))
	# 设置主刻度定位器 与 次刻度定位器
	maloc = eval(locator)
	ax.xaxis.set_major_locator(maloc)
	miloc = mp.MultipleLocator(0.1)
	ax.xaxis.set_minor_locator(miloc)

mp.show()



















