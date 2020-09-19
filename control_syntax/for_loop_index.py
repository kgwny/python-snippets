
# ループ実行するときにインデックス番号を取得するには
lst = ["a", "b", "c", "d", "e"]

# forループのなかにループカウンターを設けて都度インクリメントする方法
idx = 0
print("idx", "value")

for v in lst:
    print(idx, v)
    idx = idx + 1

# enumerate関数を使用する方法
for i, v in enumerate(lst):
    print(i, v)

# なお、インデックス番号を1から開始したいときはstart=1で指定する
for i, v in enumerate(lst, start=1):
    print(i, v)
