import functools

def add(x, y):
    return x + y

add_fixed_y = functools.partial(add, y=10)
print(add_fixed_y(2))
# 12

target_file = './tmp/tmp.txt'

open_utf_8 = functools.partial(open, encoding="utf-8")
r_open_utf_8 = functools.partial(open_utf_8, mode="r")
w_open_utf_8 = functools.partial(open_utf_8, mode="w")

with w_open_utf_8(target_file) as w:
    w.write("Hello World!")

with r_open_utf_8(target_file) as f:
    print(f.read())
