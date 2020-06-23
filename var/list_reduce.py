from functools import reduce

list_1 = [1, 2, 3, 4, 5]

# リストの最初の2要素を引数に処理を呼び出し、
# 結果と次の要素を引数に処理の呼び出しを繰り返し、
# 単一の結果を返します。

def add(x, y): return x + y

# リスト内の数値の合計
print(reduce(add, list_1))
# 15

print(reduce(lambda x, y: x + y, list_1))
# 15
