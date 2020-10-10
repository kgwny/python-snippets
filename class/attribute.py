class MyClass:
    def m(self):
        print('method')

instance = MyClass()
instance.m()
# method

instance.m = 1
print(instance.m)
# 1

# Python では、いわゆるメンバ変数やメンバ関数のこと
# をまとめて属性(attribute)と呼ぶ
