from itertools import chain

# 多次元配列を1次元の配列へ変換する
def flatten(l):
    return list(chain.from_iterable(l))

print(flatten([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]))
