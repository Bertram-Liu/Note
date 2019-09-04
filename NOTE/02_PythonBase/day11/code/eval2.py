# eval2.py

s = 'x + y'

global_dict = {'x': 1, 'y': 2}

v = eval(s, global_dict)
print('v=', v)

local_dict = {'x':100, 'y': 200}

v2 = eval(s, global_dict, local_dict)
print('v2=', v2)  # 300

v3 = eval(s, {'x': 1, 'y': 2}, {'x':100})
print('v3=', v3)  # v3 = 102
