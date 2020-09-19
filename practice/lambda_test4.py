import random

a = lambda: random.random()

# lambda式で変数なしの場合は括弧の中身は空っぽで指定
print('lambda =', a())
