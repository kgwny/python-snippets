
# 階乗
print(factorial(4))

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
