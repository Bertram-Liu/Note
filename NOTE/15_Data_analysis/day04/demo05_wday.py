"""
demo05_wday.py  时间处理
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

def dmy2wdays(dmy):
	# 把日月年字符串转为年月日字符串
	dmy = str(dmy, encoding='utf-8')
	d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	wday = d.weekday()
	return wday

# 加载文件
wdays, closing_prices = \
	np.loadtxt('../da_data/aapl.csv',
	delimiter=',', usecols=(1, 6),
	unpack=True,
	converters={1:dmy2wdays})

# 存储周一、周二、周三。。的收盘价的均值
ave_prices = np.zeros(5)
for wday in range(ave_prices.size):
	ave_prices[wday] = \
	    np.mean(closing_prices[wdays==wday])

print(ave_prices)


