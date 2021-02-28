print(type('string') is str)
# True

print(type('string') is int)
# False

# 型判定
def is_str(val):
    return type(val) is str

print(is_str('string'))
# True

print(is_str(100))
# False

print(is_str([0, 1, 2]))
# False
