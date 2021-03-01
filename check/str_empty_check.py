def empty_check(v):
    if v is None:
        print('its empty.')

def not_empty_check(v):
    if v:
        print(v)

val = None
empty_check(val)

val = 'hogehoge'
not_empty_check(val)
