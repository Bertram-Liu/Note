#   1. 模拟斗地主游戏发牌,扑克牌 54张
#     黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665)
#     红桃('\u2666')
#     数字: A2~10JQK
#     大小王
#   三个人,每个人发17张牌,底牌留三张
#     输入回车,打印第一个人的17张牌
#     输入回车,打印第二个人的17张牌
#     输入回车,打印第三个人的17张牌
#     输入回车,打印3张底牌

# 1. 生成54张牌
poker = ['大王', '小王']
kinds = ['\u2660', '\u2663', '\u2665','\u2666']
numbers = ['A']
numbers += [str(x) for x in range(2, 11)]
numbers += list("JQK")

for k in kinds:
    for n in numbers:
        poker.append(k + n)
# print(poker)
assert len(poker) == 54, '牌数不够'

# 2. 洗牌
poker2 = poker.copy()  # 复制一副新牌
import random
random.shuffle(poker2)
# print(poker2)

# 3. 发牌
player1 = poker2[:17]  # 第一个人 
player2 = poker2[17:34]
player3 = poker2[34:51]
base = poker2[51:]

# 4. 显示
input()
print('玩家1:', player1)
input()
print('玩家2:', player2)
input()
print('玩家3:', player3)
input()
print('底牌:', base)








