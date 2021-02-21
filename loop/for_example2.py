list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# forループでzip
for a, b in zip(list1, list2):
    print(a, b)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e

# zipループと辞書型(dict)の組み合わせ
zipped_dict = {}

for i, j in zip(list1, list2):
    # 2つのリストをzipした結果を辞書で取得する
    zipped_dict[i] = j

print(zipped_dict)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
