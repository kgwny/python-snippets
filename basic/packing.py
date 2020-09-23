# タプルのパッキング
t1 = ('a', 'b', 'c')
print(t1)
# ('a', 'b', 'c')

# タプルの括弧は省略が可能
t2 = 'a', 'b', 'c'
print(t2)
# ('a', 'b', 'c')

print(t1 == t2)
print(t1 is t2)

# タプルでアンパッキング
x, y, z = t1
print(x)
# 'a'
print(y)
# 'b'
print(z)
# 'c'

# リストでもアンパッキングが可能
num_list = [1, 10, 100]
i, j, k = num_list 
print(i)
# 1
print(j)
# 10
print(k)
# 100

# パッキングとアンパッキングを等号で繋いで同時に実行
x, y, z = 2, 4, 8
print(x)
# 2
print(y)
# 4
print(z)
# 8

def factorial(x):
    return x**0, x**1, x**2, x**3, x**4, x**5, x**6, x**7

v = factorial(2)
print(v)
# (1, 2, 4, 8, 16, 32, 64, 128)
print(v[3])
# 8

s = [2**x for x in range(8)]
print(s)
# [1, 2, 4, 8, 16, 32, 64, 128]
