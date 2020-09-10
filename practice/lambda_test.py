# ラムダ式

# 加算
def plus_value(num_1, num_2):
    return num_1 + num_2

print(plus_value(10, 100))

func_plus = lambda num_1, num_2: num_1 + num_2
print(func_plus(10, 100))

# 減算
def minus_value(num_1, num_2):
    return num_1 - num_2

print(minus_value(100, 10))

func_minus = lambda num_1, num_2: num_1 - num_2
print(func_minus(100, 10))
