from itertools import zip_longest

names = ['hoge','ika','tako']
age = [10,30,15]
dept = ['foo','bar','buz']

# 配列を辞書に変換する場合
new_dict = dict(zip_longest(names, age, fillvalue=25))
print(new_dict)

# タプル
for value in zip(names, age, dept):
  print(value)

# zip関数 要素番号でくっつけるやつ
for name, age, dept in zip(names, age, dept):
  print(f'{name}: {age}: {dept}')

# アスタリスクを付与すると変数がよしなに巻き取ってくれる
a, b, *c = ['foo','bar','baz','hoge','ika']
print(a,b,c)

a, *b, c = ['foo','bar','baz','hoge','ika']
print(a,b,c)
