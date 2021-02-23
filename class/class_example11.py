class Hoge(object):
    def __init__(self, x):
        self.x = x

    def f(self, y):
        return self.x + y

    def _f(self, y):
        return self.x + y + 1

    def __f(self, y):
        return self.x + y + 2

h = Hoge(1)
print(h.f(1))
# 2
print(h._f(1))
# 3
print(h._Hoge__f(1))
# 4
# print(h.__f(1))
# AttributeError: 'Foo' object has no attribute '__f'
