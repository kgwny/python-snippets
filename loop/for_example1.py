# enumerate:列挙する
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

# forループでenumerate
for i, j in enumerate(list1):
    j = list2[i]
    print(i, j)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

numbers = [1, 2, 3]
# enumerateを1からカウントしたいとき
# 第2引数にカウンターの初期値を指定する
for i, number in enumerate(numbers, 1):
    print('%d: %d' % (i, number))
# 1: 1
# 2: 2
# 3: 3
