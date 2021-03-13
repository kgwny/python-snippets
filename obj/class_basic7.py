class MyClassA:
    def funcA(self):
        print('MyClassA:funcA')

class MyClassB:
    def funcB(self):
        print('MyClassB:funcB')

# 多重継承
class MyClassC(MyClassA, MyClassB):
    pass

# 多重継承により、MyClassAクラスとMyClassBクラスのメソッドが使用できる
a = MyClassC()
a.funcA()
a.funcB()
