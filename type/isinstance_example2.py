def is_str(val):
    return isinstance(val, str)

print(is_str('string'))
# True

print(is_str(100))
# False

print(is_str([0, 1, 2]))
# False
