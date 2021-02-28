def is_str_or_int(val):
    return type(val) in (str, int)

print(is_str_or_int('string'))
# True

print(is_str_or_int(100))
# True

print(is_str_or_int([0, 1, 2]))
# False
