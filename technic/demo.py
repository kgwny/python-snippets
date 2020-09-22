
# 比較演算子を使う際、以下の2つは等価
# hoge <= 3
# hoge < 4

# 境界値で動作確認
hoge = 3
print(hoge <= 3)
print(hoge < 4)

hoge = 4
print((hoge <= 3) is (hoge < 4))
hoge = 5
print((hoge <= 3) is (hoge < 4))


a=2
b=3

# ~- は、-1
# -~ は、+1
print(a * ~-b)
# 4
print(a * -~b)
# 8

# 三項演算子
# 以下の2つは等価
if a < b:
    c = 4
else:
    c = 2
print('c =', c)

c = 4 if a < b else 2
print('c =', c)
