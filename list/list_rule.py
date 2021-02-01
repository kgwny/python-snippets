my_list1 = [1, 2, 3]

my_list2 = my_list1
print(my_list1)
# [1, 2, 3]
print(my_list2)
# [1, 2, 3]

my_list2[1] = 202

print(my_list1)
# [1, 202, 3]
print(my_list2)
# [1, 202, 3]

# リストをコピーするときはcopyメソッドを用いる
my_list1 = [1, 2, 3]
my_list2 = my_list1.copy()
my_list2[1] = 222

print(my_list1)
# [1, 2, 3]
print(my_list2)
# [1, 222, 3]


# 要素を末尾に追加するときはappendメソッドを用いる
my_list1 = [1, 2, 3]
my_list1.append(4)
print(my_list1)
# [1, 2, 3, 4]

# 指定する位置に要素を挿入するときはinsertメソッドを用いる
my_list1.insert(2, 1.5)
print(my_list1)
# [1, 2, 1.5, 3, 4]

# 指定要素を削除するときはremoveメソッドを用いる
my_list1.remove(1.5)
print(my_list1)
# [1, 2, 3, 4]

# 指定する位置の要素を削除するときはdel文を用いる
del my_list1[0]
print(my_list1)
# [2, 3, 4]

# 末尾の要素を取り出すにはpopメソッドを用いる
print(my_list1.pop())
# 4
print(my_list1)
# [2, 3]

# リストに別のリストを結合するには、extendメソッドを用いる
my_list1.extend([1, 2, 3])
print(my_list1)
# [2, 3, 1, 2, 3]
