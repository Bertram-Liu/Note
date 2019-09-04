# default_args.py


# 此示例示意函数的缺省参数的定义及调用方式
def info(name, age=1, address='不详'):
    print(name, '今年', age, '岁,家庭住址:', address)

info("魏明择", 30, '北京市朝阳区')
info("Tarena", 17)
info("小张")
# info()  # 报错
