# 配列の中にある空の要素を削除する
def ignore_empty(l):
    return list(filter(None, l))

hoge = [None, 0, 1, 2, 3, '']

print(hoge)

print(ignore_empty(hoge))
