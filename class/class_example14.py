class MyClass:
    def __init__(self):
        self.dict = dict()

    def __setitem__(self, key, value):
        print(f"set {key} {value}")
        self.dict[key] = value

    def __getitem__(self, key):
        print(f"get {key}")
        if isinstance(key, slice):
            print(key.start, key.stop, key.step)
        return self.dict[key]

c = MyClass()
print(c.dict)
# {}

c.__setitem__(0, 'a')
c.__setitem__(1, 'b')
c.__setitem__(2, 'c')
print(c.dict)
# {0: 'a', 1: 'b', 2: 'c'}

value = c.__getitem__(0)
print(value)
# a
