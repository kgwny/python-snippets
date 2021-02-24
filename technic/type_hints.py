# 型アノテーション
str1 :str = 'Hello world!'
print(str1)
print(type(str1))

int1 :int = 0
print(int1)
print(type(int1))

lis :list = ['a', 'b', 'c']
print(lis)
print(type(lis))

set1 :set = (1,1)
print(set1)
print(type(set1))

tup1 :tuple = (1, 'a')
print(tup1)
print(type(tup1))

# 引数に型アノテーションをつけることもできる
def say_hello(name: str) -> str:
    return 'Hello ' + name

print(say_hello('taro yamada'))
