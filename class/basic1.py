# メソッド
# クラスにはメソッドを定義することができます
# メソッドの定義は以下のように行います

# class クラス名:
#     def メソッド名(self):
#         #メソッドの定義

# メソッドは必ず1つ以上の引数を持ちます
# また、引数のうち最初のものはselfという名前にすることになっています
# メソッドを呼び出すには以下のようにします
# インスタンス.メソッド名()

class Test:
    def test_print(self):
        print('This is test')

test = Test()
test.test_print()
