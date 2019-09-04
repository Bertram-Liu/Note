"""
demo04_obj.py  自定义复合数据类型
"""
import numpy as np

data = [('zs', [50,51,52], 15),
		('ls', [83,71,62], 16),
		('ww', [90,91,92], 17)]

#第一种dtype的设置方式
ary = np.array(data,dtype='U2, 3int32, int32')
print(ary, ary[0][1])
print(ary[0]['f0'])

#第二种dtype的设置方式
ary = np.array(data, 
		dtype=[ ('name', 'str', 2), 
				('scores', 'int32', 3), 
				('age', 'int32', 1)])
print('-' * 45)
print(ary, ary.dtype)
print(ary[0]['age']) # 返回zs的年龄
print(ary[2]['scores']) # 返回ww的成绩

# 第三种dtype的设置方式
ary = np.array(data, dtype={
	'names':['name', 'scores', 'age'],
	'formats':['U2', '3int32', 'int32']})
print(ary)
print(ary[0]['age']) # 返回zs的年龄
print(ary[2]['scores']) # 返回ww的成绩


# 第四种dtype的设置方式
d = np.array(data, dtype={'name': ('U3', 0),
                    'scores': ('3int32', 16),
                    'age': ('int32', 28)})
print(d[0]['name'], d[0]['scores'], d.itemsize)

# ndarray数组存放日期数据
dates = ['2011-01-01', '2012-01-01', 
		 '2011-02-01', '2012', 
		 '2011-01-01 10:10:10']
ary = np.array(dates)
print(ary, ary.dtype)
ary = ary.astype('M8[D]')
print(ary, ary.dtype, ary[1]-ary[0]) 






