# リストに要素を追加する
list_1 = [i for i in range(10)]
print(list_1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 条件に一致する値のみリストに要素を追加する
list_2 = [i for i in range(10) if not i % 2 == 0]
print(list_2)
# [1, 3, 5, 7, 9]
