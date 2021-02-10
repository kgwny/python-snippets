# packing, unpacking

a, b = 2, 'str'
print(a, b)
# 2 str

x = (1, 2, 4, 8, 16)
a, b, c, d, e = x
print(a, b, c, d, e)
# 1 2 4 8 16

a, *y, e = x
print(a, e, y)
# 1 16 [2, 4, 8]

x, y, z = 2, 2, 2
print(x, y, z)

# 上の例と等価
x = y = z = 2
print(x, y, z)
