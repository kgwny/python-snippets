i = '1 2 3'

print(list(map(int, i.split(' '))))
# [1, 2, 3]

print([int(x) for x in i.split(' ')])
# [1, 2, 3]
