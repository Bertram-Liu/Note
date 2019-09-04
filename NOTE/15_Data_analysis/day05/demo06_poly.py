"""
demo06_poly.py  多项式拟合
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

# 绘制差价
diff_prices = bhp_closing_prices - vale_closing_prices
mp.plot(dates, diff_prices, color='red',
	alpha=0.4)

# 多项式拟合
days = dates.astype('M8[D]').astype('int32')
P = np.polyfit(days, diff_prices, 4)
# 计算每一天的预测值
y = np.polyval(P, days)
mp.plot(dates, y, color='green', 
	label='polyfit')


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()





