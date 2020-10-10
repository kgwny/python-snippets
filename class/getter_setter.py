class MyGetAttr:
    def __getattr__(self, name):
        print(f'{__class__.__name__}.{name}')

class MySetAttr:
    def __setattr__(self, name, value):
        print(f'{__class__.__name__}.{name} = {value}')

c = MyGetAttr()
c.hoge
# MyGetAttr.hoge

c.hoge = 1
print(c.hoge)
# 1

c = MySetAttr()
c.hoge
# Traceback (most recent call last):
# AttributeError: 'MySetAttr' object has no attribute 'hoge'
