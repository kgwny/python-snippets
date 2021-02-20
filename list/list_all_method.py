lis = []

# リストに要素追加：append
lis.append('a')
lis.append('b')
lis.append('a')
print(lis)

lis2 = lis.copy()
lis3 = lis
print(lis2)
print(lis3)

# リストの全要素クリア：clear
lis.clear()
print(lis)
print(lis2)
print(lis3)
# 重要
# copy()を使って複製したlis2は値が残る
# lis3は別の変数に代入しただけなので一緒に要素が消える

print(len(lis2))

# 特定の値を指定して要素をカウント：count
# 要素の中に'a'はいくつある？
print(lis2.count('a'))

# リストへ要素を挿入：insert
# lis3の0番目（先頭）へ'c'を挿入
lis3.insert(0, 'c')
print(lis2)

# リストの結合：extend
# lis2にlis3を結合する
lis2.extend(lis3)
print(lis2)
# ['a', 'b', 'a', 'c']

# 値の順序確認：index
# lis2の要素に最初に'b'がセットされているのは何番目？
print(lis2.index('b'))
# 1

# 一番最後の要素の取り出し：pop
print(lis2.pop())
# c
print(lis2)
# ['a', 'b', 'a']

# 値を除去：remove
# 'a'を除去する
lis2.remove('a')
print(lis2)
# 先頭にある'a'だけが消える
# ['b', 'a']

lis2.append('c')
print(lis2)
# ['b', 'a', 'c']

# リストを逆順にかえる
lis2.reverse()
print(lis2)
# ['c', 'a', 'b']

# リストを昇順にかえる
lis2.sort()
print(lis2)
# ['a', 'b', 'c']
