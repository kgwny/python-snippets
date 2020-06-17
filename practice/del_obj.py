var = 'hoge'
print(var)
# hoge

# オブジェクト削除
del var

# print(var)を実行すると
# 変数が存在しないため、エラーとなる

# nullチェックのやり方
var = None

if var is None:
    print('からっぽ')

