arr = []

# 内包表記
# 月
month = [m for m in range(1, 13)]
print(month)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

zero = [0 for m in range(10)]
print(zero)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

zero_2 = [0] * 10
print(zero_2)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 奇数
odd = [i for i in range(1, 12, 2)]
print(odd)
# [1, 3, 5, 7, 9, 11]

# 偶数
even = [i for i in range(0, 12, 2)]
print(even)
# [0, 2, 4, 6, 8, 10]

arr1 = ['a', 'b', 'c']
arr2 = ['D', 'E', 'F']

# 結合(+)
arr3 = arr1 + arr2
print(arr3)
# ['a', 'b', 'c', 'D', 'E', 'F']

# 結合(extend)
arr1.extend(arr2)
print(arr1)
# ['a', 'b', 'c', 'D', 'E', 'F']

# 四則演算
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i + 100 for i in arr])
# [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

print([i * 3 for i in arr])
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 先頭の要素
print(arr[0])
# 1

# 末尾の要素
print(arr[len(arr) - 1])
# 12
print(arr[-1])
# 12

# 最大値
print(max(arr))
# 12

# 最小値
print(min(arr))
# 1
