
def has_invalid_fields(fields):
    for field in fields:
        if field in ['foo', 'bar']:
            return False
    return True

def has_invalid_fields_short(fields):
    print(set(fields) - set(['foo', 'bar']))
    # 値が空っぽだとFalseの判定となる
    return bool(set(fields) - set(['foo', 'bar']))


hogeikatako_dict = {'hoge': 'ほげ', 'ika': 'いか', 'tako': 'たこ'}

print('===test1===')
print('hoge_dict - result =', has_invalid_fields(hogeikatako_dict))
print('hoge_dict - result =', has_invalid_fields_short(hogeikatako_dict))

foobar_dict = {'foo': 'foo', 'bar': 'bar'}

print('===test2===')
print('result =', has_invalid_fields(foobar_dict))
print('result =', has_invalid_fields_short(foobar_dict))

foobarbaz_dict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}

print('===test3===')
print('result =', has_invalid_fields(foobarbaz_dict))
print('result =', has_invalid_fields_short(foobarbaz_dict))
