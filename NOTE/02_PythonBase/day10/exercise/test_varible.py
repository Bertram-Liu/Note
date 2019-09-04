a = 1
L = [1]

def fn(a, L):
    a += 2
    L += [2]

fn(a, L)
print(a, L)  # 1, [1, 2]

