a = b = 'foo'
print(a == b)
# True
print(a is b)
# True

a = b = 'f o o'
print(a == b)
# True
print(a is b)
# True

a = b = 'x+y'
print(a == b)
# True
print(a is b)
# True

a = b = '/'
print(a == b)
# True
print(a is b)
# True

a = 'f'
a += 'oo'
b = 'foo'
print(a == b)
# True
print(a is b)
# False
