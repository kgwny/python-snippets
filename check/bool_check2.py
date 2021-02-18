print(isinstance(False, bool))
# True
print(isinstance(False, int))
# True

print(False == 0)
# True
print(False is 0)
# False(SyntaxWarning)

print(True == 1)
# True
print(True is 1)
# False(SyntaxWarning)

print(True + True)
# 2

result = -1
print('OK' if result == 0 else 'NG')
# NG

print(('NG', 'OK')[result == 0])
# NG

result = 0
print(('NG', 'OK')[result == 0])
# OK
