list = [0, 2, 1, 4, 2, 3, 2] 

# 2を検索 x=2の位置を抽出する
indexes = [i for i, x in enumerate(list) if x == 2]

print(indexes)
# [1, 4, 6]
