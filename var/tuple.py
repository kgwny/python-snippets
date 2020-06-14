
# tuple is immutable
t1 = ('v','a','r')

print(type(t1))
# <class 'tuple'>
print(t1)
# ('v', 'a', 'r')
print(len(t1))
# 3

# 値の取得 0要素目を取得
print(t1[0])
# 'v'
print(type(t1[0]))
# <class 'str'>


# 値の取得 先頭の2要素を取得
print(t1[:2])
# ('v', 'a')


# 要素が1つのみの場合
t2 = ('s',)

print(type(t2))
# <class 'tuple'>
print(t2)
# ('s',)
print(len(t2))
# 1


# 連結は可能
t0 = t1 + t2

print(type(t0))
# <class 'tuple'>
print(t0)
# ('v', 'a', 'r', 's')
print(len(t0))
# 4
