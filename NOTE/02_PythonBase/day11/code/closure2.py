# closure.py

# 此示例示意用局部变量 money 来保存数据
def child_buy(obj, m):
    '''m 代表物品 obj 的价格'''
    money = 1000  # 家长给孩子压岁钱1000元
    if m < money:
        money -= m
        print('买', obj,'花了', m, '元剩余', money, '元')
    else:
        print('钱不够，买', obj, '失败')

child_buy('变形金刚', 200)
money = 0
child_buy('漫画三国', 100)
child_buy('手机', 1300)




