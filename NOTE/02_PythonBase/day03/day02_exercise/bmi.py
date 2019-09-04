#   4 BMI指数(Body Mass Index)  又称 身体质量指数
#      BMI公式:   BMI = 体重(公斤) / 身高的平方(米)
#      如: 一个69公斤的人,身高是173公分
#          BMI = 69 / 1.73 ** 2 = 23.05
#     标准表:
#       BMI < 18.5         体重过轻
#       18.5 <= BMI <= 24  正常范围
#       BMI > 24           体重过重
#     输入身高和体重,打印BMI的值,并打印体重状况

kg = float(input("请输入体重(公斤): "))
meter = float(input("请输入身高(米): "))

bmi = kg / meter ** 2
print("BMI=", bmi)

if bmi < 18.5:
    print('您的体重过轻')
elif 18.5 <= bmi <= 24:
    print("您的体重正常")
else:
    print("您的体重过重")

