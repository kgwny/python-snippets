class MyClass:
    def hello(self):
        print('Hello')

# 親クラスのhello()メソッドをオーバーライド
class MyClass2(MyClass):
    def hello(self):
        print('HELLO')

c1 = MyClass()
c1.hello()
# Hello

c2 = MyClass2()
c2.hello()
# HELLO
