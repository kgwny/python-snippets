# 関数を引数にとる関数
def proc(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print(add(2, 1))
# 3
print(add(2, 1))
# 1
print(proc(add, 3, 1))
# 4
print(proc(sub, 3, 1))
# 2
