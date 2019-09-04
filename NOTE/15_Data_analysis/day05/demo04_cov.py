"""
demo04_cov.py  协方差
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
dates, bhp_closing_prices = \
    np.loadtxt('../da_data/bhp.csv',
	delimiter=',', usecols=(1, 6),
	unpack=True, dtype='M8[D], f8',
	converters={1:dmy2ymd})
vale_closing_prices = \
    np.loadtxt('../da_data/vale.csv',
	delimiter=',', usecols=(6,),
	unpack=True)

# 绘制折线图
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
# 设置刻度定位器
ax = mp.gca()
#每周一一个主刻度
maloc = md.WeekdayLocator(byweekday=md.MO)
ax.xaxis.set_major_locator(maloc)
# 设置主刻度日期的格式
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y-%m-%d'))

#DayLocator:每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())

# 把dates的数据类型改为matplotlib的日期类型
dates = dates.astype(md.datetime.datetime)

# 绘制收盘价
mp.plot(dates, bhp_closing_prices, 
	label='BHP Closing Prices', linewidth=2,
	color='dodgerblue', linestyle='-')

# 绘制收盘价
mp.plot(dates, vale_closing_prices, 
	label='VALE Closing Prices', linewidth=2,
	color='orangered', linestyle='-')

# 计算两个股票的协方差
bhp_mean = np.mean(bhp_closing_prices)
vale_mean = np.mean(vale_closing_prices)
# 离差
d1 = bhp_closing_prices - bhp_mean
d2 = vale_closing_prices - vale_mean
cov = np.mean(d1*d2)
print(cov)

# 计算相关系数
s = cov / (np.std(bhp_closing_prices)* \
	       np.std(vale_closing_prices))
print(s)

# 获取相关性矩阵
m = np.corrcoef(bhp_closing_prices, vale_closing_prices)
print(m)
# 获取协方差矩阵
cm = np.cov(bhp_closing_prices, vale_closing_prices)
print(cm)

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()





