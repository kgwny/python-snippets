class Hoge:
    # クラス内変数(private)
    __attr = 100

    # コンストラクタ
    def __init__(self):
        self.__attr = 999

    # publicメソッド
    def method(self):
        self.__method()

    # privateメソッド
    def __method(self):
        print(self.__attr)

hoge = Hoge()
hoge.method()
# hoge.__method() # 実行時エラーとなる
# hoge.__attr     # 実行時エラーとなる
