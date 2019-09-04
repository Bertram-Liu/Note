# exec.py


s = '''
fx = lambda n: (n ** 2 + 1) % 5 == 0

print(fx(3))  # True
print(fx(4))  # False
'''

exec(s)