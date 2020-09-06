# __init__() メソッド
# コンストラクタ
# クラスのインスタンスが生成されたときに呼び出される

class MyClass:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

a = MyClass("なまえ")
print(a.getName())
# なまえ
