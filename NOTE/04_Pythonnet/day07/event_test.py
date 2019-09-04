from threading import Event 

# 创建事件对象
e = Event()

e.set()  # 设置e

e.clear() # 清除e设置

e.wait(3)

print(e.is_set())

print("************************")