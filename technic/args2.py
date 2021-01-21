# 可変長引数
# 関数の引数に**をつけると可変長引数となります。
# kwargs = key word argument

def something(**kwargs):
  print(kwargs)

something(hoge=100, tako=200, ika=300)
# {'hoge': 100, 'tako': 200, 'ika': 300}
