
# リスト型
list_1 = [1, 2]

print(type(list_1))
# <class 'list'>

print(list_1)
# [1, 2]

list_2 = [3, 4]
print(list_2)
# [3, 4]

# listの結合
list_3 = list_1 + list_2
print(list_3)
# [1, 2, 3, 4]

# listのコピー
list_4 = list_3.copy()
print(list_4)
# [1, 2, 3, 4]

# listのクリア
list_3.clear()
print(list_3)
# []

# listの末尾に値を追加
list_4.append(5)
print(list_4)
# [1, 2, 3, 4, 5]

# listの先頭に値を追加
# 0番目の要素に"hoge"を追加
list_4.insert(0, 'hoge')
# 1番目の要素に"fuga"を追加
list_4.insert(1, 'fuga')
print(list_4)
# ['hoge', 'fuga', 1, 2, 3, 4, 5]
