import random

# ランダムな数字(float)を取得する
rand_func = lambda: random.random()
print(rand_func())

# 
f = lambda x, *args, key, **kwargs: [key, args, kwargs]
print(f(1, 2, 3, 4, 5, key='abakamu', name='piyopiyo', author='kgwny'))
# ['abakamu', (2, 3, 4, 5), {'name': 'piyopiyo', 'author': 'kgwny'}]
