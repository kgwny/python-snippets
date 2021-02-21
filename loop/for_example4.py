# range(start, stop, step)

for i in range(0, 10, 1):
    print(i)

# else:forループが終了すると実行する
for i in range(0, 10, 2):
    print(i)
else:
    print('糸冬')

# break:途中でループを抜ける
# continue:ループを継続する
for i in range(0, 10, 2):
    print(i)
    if i == 8:
        break
    else:
        continue
