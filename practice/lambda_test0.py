# lambda 引数: 返り値

def add_hoge(s):
    return s + 'hoge'

hoge = lambda s: s + 'hoge'

print(add_hoge('hoge'))
print(hoge('hoge'))
print(add_hoge('hoge') == hoge('hoge'))
