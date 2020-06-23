list_1 = [1, 2, 3]

print([x * 2 for x in list_1])
# [2, 4, 6]

print([x * 2 for x in list_1 if x == 3])
# [6]

print([[x, x * 2] for x in list_1])
# [[1, 2], [2, 4], [3, 6]]

print([(x, x * 2) for x in list_1])
# [(1, 2), (2, 4), (3, 6)]

list_2 = [4, 5, 6]

print([x * y for x in list_1 for y in list_2])
# [4, 5, 6, 8, 10, 12, 12, 15, 18]

print([list_1[i] * list_2[i] for i in range(len(list_1))])
# [4, 10, 18]
