# 可変長引数
# 関数の引数に*をつけると可変長引数となる

def something(*args):
  print(args)

something('hoge', 'fuga', 'tako')
# ('hoge', 'fuga', 'tako')
