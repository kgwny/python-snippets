# for loop

# 0,1,2
for i in range(3):
    print(i)
else:
    print('for in range 終了')

# 1,2,3
for i in [1, 2, 3]:
    print(i)
else:
    print('for in 配列 終了')

# あいうえお
for char in u'あいうえお':
    print(char)
else:
    print('for in 文字列 終了')

# 0,1 breakにより2は出ない
for i in range(3):
    if i == 2:
        break
    print(i)
else:
    print('breakがある場合はelseに到達しない')

# 0,2 continueにより1が飛ばされる
for i in range(3):
    if i == 1:
        continue
    print(i)
 