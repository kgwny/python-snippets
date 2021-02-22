lis = [(1, 'a'), (2, 'b'), (3, 'c')]
print(type(lis))
# <class 'list'>

a1, b1 = zip(*lis)
print(a1, b1)
# (1, 2, 3) ('a', 'b', 'c')

dic = dict(zip(a1, b1))
print(dic)
# {1: 'a', 2: 'b', 3: 'c'}

lis = list(zip(*lis))
print(lis)
# [(1, 2, 3), ('a', 'b', 'c')]

tup = tuple(zip(*lis))
print(tup)
# ((1, 2, 3), ('a', 'b', 'c'))

lis_1 = [1, 2, 3]
lis_2 = ['a', 'b', 'c']
dic = dict(zip(lis_1, lis_2))
print(dic)
# {1: 'a', 2: 'b', 3: 'c'}
