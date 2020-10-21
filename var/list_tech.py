# a, b, c = ['Tom','Peter','Taro','Chris']
# エラーになる

# ひとつ目とふたつ目を文字列で取得、それ以降をリストで取得
a, b, *c = ['Tom','Peter','Taro','Chris']
print(a,b,c)
# Tom Peter ['Taro', 'Chris']

# 先頭と末尾を文字列で取得、それ以外はリストで取得
a, *b, c = ['Tom','Peter','Taro','Chris']
print(a,b,c)
# Tom ['Peter', 'Taro'] Chris

# 先頭と末尾のみ抽出する
a, *_, c = ['Tom','Peter','Taro','Chris']
print(a,c)
# Tom Chris
