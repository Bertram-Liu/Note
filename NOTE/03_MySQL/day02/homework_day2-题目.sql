-- homework_day2.sql
-- MySQL第二天作业

1. 创建数据库bank, 并指定为utf8编码格式

2. 创建账户表(acct, utf8编码格式), 包含如下字段
	acct_no   	账号，字符串类型，长度32字节
	acct_name 	户名，字符串类型，长度128字节
	cust_no   	客户编号，字符串类型，长度32字节
	acct_type	账户类型, 整数型(1-存款账户 2-贷款账户)
	reg_date	开户日期, 日期类型
	status		账户状态(1-正常 2-注销 3-挂失 4-冻结)
	balance   	数字类型，最长16位，2位小数

3. 至少插入五笔数据(要求数据尽量看上去真实) 

4. 编写如下SQL语句 
1)查找某个客户账户信息
2)查找余额大于等于5000的账户信息
3)查找余额大于等于5000的贷款账户信息
4)查找账户名称以'D'开头的所有账户信息
5)查找所有账户信息，并按照金额倒序排列
6)统计每种状态的账户笔数
7)查询账户余额的最大值、最小值、平均值、总金额
8)查询账户余额最大的前3笔订单

