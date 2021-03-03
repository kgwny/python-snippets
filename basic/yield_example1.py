# yieldの使い方
def func():
    a = 10
    b = 20
    c = a + b
    yield c      # ここで一旦停止してcを返却

    a = 100
    b = 200
    c = a + b
    yield c      # ここで一旦停止してcを返却

    a = 1000
    b = 2000
    c = a + b
    yield c      # ここで一旦停止してcを返却

for x in func():
    print(x)
