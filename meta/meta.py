if __name__ == "__main__":

    class Metaclass(type):
        def __new__(mcs, name, bases ,namespace):
            print(mcs,'__new__()')
            return super().__new__(mcs, name, bases, namespace)

        @classmethod
        def __prepare__(mcs, name, bases,**kwargs):
            print(mcs,'__prepare__()')
            return super().__prepare__(mcs, name, bases,**kwargs)

        def __init__(cls,name, bases, namespace, **kwargs):
            print(cls,'__init__()')
            super().__init__(name, bases, namespace)

        def __call__(cls, *args, **kwargs):
            print(cls,'__call__()')
            return super().__call__(*args, **kwargs)

    class RevealingClass(metaclass=Metaclass):
        def __new__(cls):
            print(cls,'__new__')
            return super().__new__(cls)

        def __init__(self):
            print(self,'__init__')
            super().__init__()
