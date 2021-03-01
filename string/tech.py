# 文字列のかけ算
print('hoge' * 2)

# 文字列の結合
s = 'ika'
s+= 'tako'
print(s)

# 負のインデックスを指定してリストから値を抽出
list_a = ['a', 'b', 'c', 'd']
print(list_a[-1])
# d
print(list_a[-2])
# c

# 2つの変数の値を入れ替える
a = 'artifact'
b = 'biography'
a, b = b, a
print(a)
# biography
print(b)
# artifact

# 複数の変数に同一値を格納する
a = b = 'same'
print(a)
# same
print(b)
# same

# 複数の変数に複数の値を一括で格納する
a, b = 'artifact', 'biography'
print(a)
# artifact
print(b)
# biography
