# list to dict
l = ['foo=hoge','bar=ika','baz=tako']
d = dict(s.split('=') for s in l)
print(d)
# {'foo': 'hoge', 'bar': 'ika', 'baz': 'tako'}
