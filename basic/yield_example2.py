# yieldの使い方その２
def function():
    a = 'hoge'
    yield a

    b = 'piyo'
    yield a + b

    c = 'fuga'
    yield a + b + c

for x in function():
    print(x)
