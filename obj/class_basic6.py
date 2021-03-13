# スーパークラスの例
class MyClass1(object):
    def __init__(self):
        self.val1 = 123

class MyClass2(MyClass1):
    # super()により親クラスを参照する
    # 第一引数にクラス、第二引数にインスタンスを指定する
    def __init__(self):
        # サブクラスのコンストラクタで親クラスのコンストラクタをコールする
        super(MyClass2, self).__init__()
        self.val2 = 456

a = MyClass2()
print(a.val1)
# 123
print(a.val2)
# 456
