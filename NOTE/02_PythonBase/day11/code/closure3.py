# closure.py

# 此示例示意用外部嵌套函数的变量 money 来保存钱数
def give_yashiqian(m):
    money = m
    def child_buy(obj, m):
        '''m 代表物品 obj 的价格'''
        nonlocal money
        if m < money:
            money -= m
            print('买', obj,'花了', m, '元剩余', money, '元')
        else:
            print('钱不够，买', obj, '失败')
    return child_buy

cb = give_yashiqian(1000)  # 家长给孩子压岁钱1000元

cb('变形金刚', 200)
money = 0
cb('漫画三国', 100)
cb('手机', 1300)




