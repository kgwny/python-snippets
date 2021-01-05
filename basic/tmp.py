lst = ["a", "b", "c", "d", "e"]
idx = 0
for v in lst:
    print(idx, v)
    idx = idx + 1

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

for i, v in enumerate(lst):
    print(i, v)

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

for i, v in enumerate(lst, start=5):
    print(i, v)

# 5 a
# 6 b
# 7 c
# 8 d
# 9 e

a_lst = ["a", "b", "c", "d", "e"]
b_lst = [1, 2, 3, 4, 5]
for a, b in zip(a_lst, b_lst):
    print(a, b)
 
# a 1
# b 2
# c 3
# d 4
# e 5

for i, a in enumerate(a_lst):
    b = b_lst[i]
    print(a, b)
 
# a 1
# b 2
# c 3
# d 4
# e 5

dic = {}
for a, b in zip(a_lst, b_lst):
    dic[a] = b

print("---")
print(dic)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
