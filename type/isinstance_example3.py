def is_str_or_int(val):
    return isinstance(val, (int, str))

print(is_str_or_int('string'))
# True

print(is_str_or_int(100))
# True

print(is_str_or_int([0, 1, 2]))
# False
