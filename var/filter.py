list_1 = [1, 2, 3]

def isodd(x): return x % 2

print(list(filter(isodd, list_1)))
# [1, 3]

print(list(filter(lambda x: x % 2, list_1)))
# [1, 3]

print([x for x in list_1 if x % 2])
# [1, 3]
