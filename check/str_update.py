b = 'foo'
print(b[0])
print(b[1])
print(b[2])

b[0] = 'h'
# できない
# TypeError: 'str' object does not support item assignment

# a = (1, 2, 3)
# a[0] = 0
# TypeError: 'tuple' object does not support item assignment
