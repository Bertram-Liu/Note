"""
demo04_std.py  标准差
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

def dmy2ymd(dmy):
	# 把日月年字符串转为年月日字符串
	dmy = str(dmy, encoding='utf-8')
	d = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	ymd = d.strftime('%Y-%m-%d')
	return ymd


# 加载文件
dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, \
volumns = np.loadtxt('../da_data/aapl.csv',
	delimiter=',', usecols=(1, 3, 4, 5, 6, 7),
	unpack=True, dtype='M8[D], f8, f8, f8, f8, f8',
	converters={1:dmy2ymd})

std = np.std(closing_prices)
print('std:', std)

m = np.mean(closing_prices)
d = closing_prices - m
q = d**2 
s = np.mean(q)
v = np.sqrt(s)
print(v)






