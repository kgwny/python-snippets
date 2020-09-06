# __del__() メソッド
# デストラクタ
# クラスのインスタンスが消滅するときに呼び出される

class MyClass:
    def __init__(self):
        print("初期化します")

    def __del__(self):
        print("消えます")

a = MyClass()
# 初期化します
del a
# 消えます
