import functools

# 引数が固定の関数
def add(x, y):
    return x + y

add_fixed_y = functools.partial(add, y=3)
print(add_fixed_y(2))
# 5

# functools
# https://docs.python.org/ja/3/library/functools.html
