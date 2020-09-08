# 多重継承サンプル
class A:
    def hello(self):
        print('Hello from A')

class B(A):
    pass

class C:
    def hello(self):
        print('Hello from C')

class D(B, C):
    pass

d = D()
d.hello()
# Hello from A
