a = set([1, 3, 2])
b = set([1, 3, 2])
c = set([1, 2, 3, 2])

print(a == b)
# True
print(a is b)
# False

print(a == c)
# True
# 順序の情報を保持せず、ユニークな値しか持たないため
print(a is c)
# False
