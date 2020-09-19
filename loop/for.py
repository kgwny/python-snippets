
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]

# forループでzip
for a, b in zip(list1, list2):
    print(a, b)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e

# forループでenumerate
for i, j in enumerate(list1):
    j = list2[i]
    print(i, j)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
