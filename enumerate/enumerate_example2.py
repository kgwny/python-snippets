tup = ('a', 'b', 'c')
lis = ['A', 'B', 'C']

for i in enumerate(zip(tup, lis), 1):
    print(i)
# (1, ('a', 'A'))
# (2, ('b', 'B'))
# (3, ('c', 'C'))

lis_1 = [1, 2, 3]
lis_2 = ['hoge', 'fuga', 'piyo']

for i, j in enumerate(zip(lis_1, lis_2), 1):
    print(i, j)
# 1 (1, 'hoge')
# 2 (2, 'fuga')
# 3 (3, 'piyo')
