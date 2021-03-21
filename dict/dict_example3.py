# 空のdict
dic = {}
print(dic)
# {}

# dictに要素を追加する
dic['key1'] = 'val1'
print(dic)
# {'key': 'val'}

# __setitem__を用いてdictに要素を追加する
# dic[key] = value は
# dic.__setitem__(key, value)と等価

dic.__setitem__('key2', 'val2')
print(dic)
# {'key1': 'val1', 'key2': 'val2'}
