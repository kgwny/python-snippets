def hoge(*args):
  # 関数の引数に*をつけると可変長引数となります。
  print(args)

hoge("Aさん", "Bさん", "Cさん")
# => ('Aさん', 'Bさん', 'Cさん')

def fuga(**kwargs):
  # *を二つ繋げると可変長引数となります。
  # kwargsはkey word argumentの意味だと思います。
  print(kwargs)

fuga(A=1000, B=2000, C= 3000)
# => {'A': 1000, 'B': 2000, 'C': 3000}


def hogefuga(*args, **kwargs):
  # 組み合わせ可能です
  print(args)
  print(kwargs)

hogefuga(1, 2, 3, 4, A='a', B='b', C='c')
# => (1, 2, 3, 4)
# => {'A': 'a', 'B': 'b', 'C': 'c'}

def hoge2(a, b, *, c, d):
  # アスタリスクを一つ引数に加えると、以降の引数はキーワード引数扱いとなる
  print(a, b, c, d)

hoge2(1, 2, c='c', d='d')
# => 1 2 c d

# 引数を指定しない場合はTypeError
# hoge2(1, 2)
# => Traceback (most recent call last):
# =>   File "<stdin>", line 1, in <module>
# => TypeError: hoge() missing 2 required keyword-only arguments: 'c' and 'd'
# cとdのキーワード引数は必須です。的なエラーですね。
