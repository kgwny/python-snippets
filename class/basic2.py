# コンストラクタとデストラクタ
# インスタンス生成されるときに自動的に呼び出されるメソッドのことをコンストラクタといいます
# コンストラクタを定義するには"__init__"という名前でメソッドを作成します

# class Test:
#     def __init__(self, 引数1, 引数2, ….):
#         #コンストラクタの定義
# 
# __init__もselfという引数が必要になります
# self以外にも引数を追加することができます
# インスタンス生成する際、クラスを呼び出す時の引数が渡されます

class Test1:

    def __init__(self, num):
        self.num = num

    def print_num(self):
        print('引数で渡された数字は{}です'.format(self.num))

test = Test1(10)
test.print_num() 

# インスタンスが不要になり削除される時に呼ばれるメソッドをデストラクタといいます
# デストラクタは"__del__"という名前のメソッドで定義されます

class Test2:

    def __init__(self):
        print('コンストラクタがコールされました')

    def __del__(self):
        print('デストラクタがコールされました')

test = Test2()
del test
