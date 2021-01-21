# アスタリスクを一つ引数に加えると、以降の引数はキーワード引数扱いとなる
def something(a, b, *, c, d):
  print(a, b, c, d)

something(a=1, b=2, c=3, d=4)
# 1 2 3 4

something(1, 2, c=3, d=4)
# 1 2 3 4

# something(1, 2, 3, 4)
# errorになる
