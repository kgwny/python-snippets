class Hoge:
    def __init__(self, *args):
        self.x, self._y, self.__z = args

hoge = Hoge(1, 2, 4)
print(hoge.x)
# 1

# print(hoge._y)
# 動くけどNG

# print(hoge.__z)
# エラーになる
