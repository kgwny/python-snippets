def proc(func, x, y):
    return func(x, y)

print(proc(lambda a, b: a + b, 4, 3))
# 7
print(proc(lambda a, b: a - b, 4, 3))
# 1
