
# zipループと辞書型(dict)の組み合わせ
dict = {}

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

for i, j in zip(list1, list2):
    dict[i] = j

print(dict)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
