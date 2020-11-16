
var = 10

if var == 10:
    print('OK')
else:
    print('NG')

print('OK') if var == 10 else print('NG')

print(['NG', 'OK'][var == 10])


hoge = 10
piyo = 10

if hoge == 10 and piyo == 10:
    print('both')
elif hoge != 10 and piyo != 10:
    print('neither')
else:
    print('either')

print(['neither', 'either', 'both'][(hoge == 10) + (piyo == 10)])
