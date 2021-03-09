class C:

    def __init__(self, arg): # コンストラクター
        self.value = arg

    def __add__(self, other): # +演算子
        return C(self.value + other.value)

    def __repr__(self): # REPLで表示される文字列を返すメソッド
        return f"C({self.value})"

c1 = C(1)
c2 = C(2)
s = c1 + c2 # __add__の呼び出し
print(s)
