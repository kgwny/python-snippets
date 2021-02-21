# 逆順にループ処理
for i in reversed(range(1, 6, 2)):
    print(i)
# 5
# 3
# 1

for i in reversed(range(2, 6, 1)):
    print(i)
# 5
# 4
# 3
# 2

# リストの逆順ループ
values = ['a', 'b', 'c']
for value in reversed(values):
    print(value)
# c
# b
# a

# 上のロジックと等価
for value in values[::-1]:
    print(value)
# c
# b
# a
