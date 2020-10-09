class cached_property(object):
    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, parent, klass):
        if parent is None:
            return self
        value = parent.__dict__[self.func.__name__] = self.func(parent)
        return value

class Hoge(object):
    @cached_property
    def value(self):
        import time
        time.sleep(10)
        return 'What a heavy process!'

hoge = Hoge()
print(hoge.value)
print(hoge.value)
