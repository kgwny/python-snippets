class MyClass:
    def __index__(self):
        return 1

a = ['aa', 'bb', 'cc']

# インスタンス生成
i = MyClass() 
print(i)
# <__main__.MyClass object at 0x10fd43250>
print(a[i])
# bb
