
# 辞書をswitch文の代わりとして使う

# 足し算
def add(a, b):
    return a + b

# 引き算
def subtract(a, b):
    return a - b

# 辞書型の変数a,b
a = {
    True: 1,
    False: -1,
    None: 0
}

b = {
    '+': add,
    '-': subtract
}

print(a.get(True, 0))
# 1

print(a.get(False, 0))
# -1

print(a.get(None, 0))
# 0

print(b['+'](1, 2))
# 3

print(b['-'](1, 2))
# -1
