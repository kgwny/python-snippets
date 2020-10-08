class DescriptorTest:

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

class MyClassTest:
    a = DescriptorTest()

if __name__ == "__main__":
    test = MyClassTest()
    test.a = 'hoge'
    print(test.a)
