# test_mymod.py


# 此示例示意导入自定义的模块mymod ,然后调用mymod
# 内部的函数和数据

import mymod

mymod.myfac(5)  # 调用同mymod里的myfac函数

from mymod import mysum

mysum(100)

from mymod import *
print(name1)
print(name2)
