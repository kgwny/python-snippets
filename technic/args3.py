# 可変長引数
# ２つ使うこともできる

def something(*args, **kwargs):
  print(args)
  print(kwargs)

something(1, 2, 3, 4, hoge='a', ika='b', tako='c')
# (1, 2, 3, 4)
# {'hoge': 'a', 'ika': 'b', 'tako': 'c'}
