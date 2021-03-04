def infinite_one():
    while True:
        yield 1

# 無限ループ
for x in infinite_one():
    print(x)
