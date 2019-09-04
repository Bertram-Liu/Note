# mymod3.py

# 当用from mymod3 import *导放此模块时,隐藏属性:
# _f1, _f2, _name, __name 不会被导入

def myfunc():
    _f1()
    _f2()

def _f1():
    print("_f1")

def _f2():
    print("_f2")

name = 100
_name = 200
__name = 300

