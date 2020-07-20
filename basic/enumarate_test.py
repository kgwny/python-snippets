names = ['hoge','tako','ika']
index = 0

for name in names:
  print(index, name)
  index +=1

# 上と下の処理は同じ

names = ['hoge','tako','ika']

for index, name in enumerate(names):
  print(index, name)

# indexを1始まりにしたいとき
for index, name in enumerate(names, start=1):
  print(index, name)

# 辞書型にしたいとき
new_dict = dict(enumerate(names))
print(new_dict)
